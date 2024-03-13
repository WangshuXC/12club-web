from flask import Flask, jsonify, request, make_response
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    create_access_token,
    create_refresh_token,
    get_jwt,
    set_access_cookies,
    set_refresh_cookies,
    jwt_required,
    get_jwt_identity,
)
from models import User, Anime
from settings import db
import math
from datetime import timedelta, datetime
import os 


app = Flask(__name__)

# Setup the Flask-JWT-Extended
app.config["JWT_SECRET_KEY"] = "12345678"
jwt = JWTManager(app)


class LoginApi(Resource):
    @jwt_required(optional=True)
    def post(self):
        current_token = get_jwt()
        if current_token:
            return {"message": "You are already logged in"}, 200
        parser = reqparse.RequestParser()
        parser.add_argument(
            "username", type=str, required=True, help="Username is required"
        )
        parser.add_argument(
            "password", type=str, required=True, help="Password is required"
        )
        args = parser.parse_args()
        username = args["username"]
        password = args["password"]
        user = User.query.filter_by(username=username).first()
        if user and user.verify_password(password):
            # Create the tokens we will be sending back to the user
            access_token = create_access_token(identity=username)
            refresh_token = create_refresh_token(identity=username)

            # Create the response with current time and cookie expiration times
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            resp = {
                "login": True,
                "current_time": current_time,
            }
            resp = make_response(jsonify(resp), 200)

            set_access_cookies(resp, access_token, timedelta(minutes=15))
            set_refresh_cookies(resp, refresh_token, timedelta(hours=1))
            return resp
        else:
            return {"message": "Invalid username or password"}, 401


class RefreshTokenApi(Resource):
    @jwt_required
    def post(self):
        # Create the new access token
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)

        # Set the JWT access cookie in the response
        resp = jsonify({"refresh": True})
        set_access_cookies(resp, access_token)
        return resp, 200


class SignupApi(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "username", type=str, required=True, help="Username is required"
        )
        parser.add_argument(
            "password", type=str, required=True, help="Password is required"
        )
        args = parser.parse_args()
        username = args["username"]
        password = args["password"]

        user = User().new_user(username, password)
        db.session.add(user)
        db.session.commit()
        return {"message": "Signup success"}, 201
    

    
# 上传文件到data目录
class UploadApi(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('file', type=FileStorage, location='files', required=True, help="File is required")
        parser.add_argument('cover', type=FileStorage, location='files', required=True, help="Cover is required")
        parser.add_argument('title', type=str, required=True, help="Title is required")
        parser.add_argument('description', type=str, required=True, help="Description is required")
        parser.add_argument('type', type=str, required=True, help="Type is required")
        args = parser.parse_args()

        file = args['file']
        cover = args['cover']
        title = args['title']
        description = args['description']
        type = args['type']

        filename = secure_filename(file.filename)
        covername = secure_filename(cover.filename)

        file.save(os.path.join('data',type, title, filename))
        cover.save(os.path.join('data',type, title, covername))

        # TODO: Save title and description to database

        return {"message": "File and cover uploaded successfully, title and description saved"}, 201


class HomeApi(Resource):
    def get(self):
        return {"message": "Hello, World!"}


class AnimeApi_page(Resource):
    def get(self, animepage_id=None):
        if animepage_id:
            # 捕获请求中的 orderby 参数
            sort = request.args.get("sort", "view_count")
            orderby = request.args.get("orderby", "desc")

            # 计算offset值
            items_per_page = 20
            offset = (int(animepage_id) - 1) * items_per_page

            # 根据sort和orderby参数动态构建排序表达式
            if sort in ["view_count", "download_count", "update_date"]:
                sort_field = getattr(Anime, sort)
            else:
                sort_field = Anime.id

            if orderby == "desc":
                sort_expression = sort_field.desc()
            else:  # 默认使用升序
                sort_expression = sort_field.asc()

            # 查询指定范围内的动漫数据
            anime_page_list = (
                Anime.query.order_by(sort_expression)
                .offset(offset)
                .limit(items_per_page)
                .all()
            )
            anime_count = Anime.query.count()
            total_page = math.ceil(anime_count / items_per_page)
            # 将查询结果转换成字典列表
            results = [
                {
                    "id": anime.id,
                    "title": anime.title,
                    "cover": anime.cover,
                }
                for anime in anime_page_list
            ]
            result = {"total_page": total_page, "results": results}
            return result, 200
        else:
            return {"message": "Anime not found"}, 404


class AnimeApi_detail(Resource):
    def get(self, anime_id=None):
        if anime_id:
            # 根据 ID 获取特定的动漫信息
            anime = Anime.query.get(anime_id)
            if anime:
                return {
                    "id": anime.id,
                    "title": anime.title,
                    "episode_count": anime.episode_count,
                    "title_another": anime.title_another,
                    "title_japanese": anime.title_japanese,
                    "description": anime.description,
                    "isover": anime.isover,
                    "release_date": anime.release_date.isoformat(),
                    "update_date": anime.update_date.isoformat(),
                    "view_count": anime.view_count,
                    "download_count": anime.download_count,
                }, 200
            else:
                return {"message": "Anime not found"}, 404
        else:
            # 返回表内所有的动漫信息
            anime_list = Anime.query.all()
            return [
                {
                    "id": anime.id,
                    "title": anime.title,
                    "title_another": anime.title_another,
                    "title_japanese": anime.title_japanese,
                    "description": anime.description,
                    "release_date": anime.release_date.isoformat(),
                    "update_date": anime.update_date.isoformat(),
                    "view_count": anime.view_count,
                    "download_count": anime.download_count,
                }
                for anime in anime_list
            ]

    def post(self):
        # 创建新的动漫信息
        data = request.json
        anime = Anime(
            title=data["title"],
            description=data["description"],
            release_date=data["release_date"],
            update_date=data.get("update_date"),
            view_count=data.get("view_count", 0),
            download_count=data.get("download_count", 0),
        )
        db.session.add(anime)
        db.session.commit()
        return {"message": "Anime created successfully"}, 201

    def put(self, anime_id):
        # 更新动漫信息
        anime = Anime.query.get(anime_id)
        if anime:
            data = request.json
            anime.title = data.get("title", anime.title)
            anime.description = data.get("description", anime.description)
            anime.release_date = data.get("release_date", anime.release_date)
            anime.update_date = data.get("update_date", anime.update_date)
            anime.view_count = data.get("view_count", anime.view_count)
            anime.download_count = data.get("download_count", anime.download_count)
            db.session.commit()
            return {"message": "Anime updated successfully"}
        else:
            return {"message": "Anime not found"}, 404

    def delete(self, anime_id):
        # 删除动漫信息
        anime = Anime.query.get(anime_id)
        if anime:
            db.session.delete(anime)
            db.session.commit()
            return {"message": "Anime deleted successfully"}
        else:
            return {"message": "Anime not found"}, 404


class UserApi(Resource):
    def get(self):
        users = db.session.query(User).all()
        result = [{"id": user.id, "name": user.name} for user in users]
        return {"users": result}
