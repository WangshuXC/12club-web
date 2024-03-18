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
from models import User, Anime, Comment
from settings import db, DATA_PATH
import math
from datetime import timedelta, datetime
import os


app = Flask(__name__)

# Setup the Flask-JWT-Extended
app.config["JWT_SECRET_KEY"] = "12345678"
jwt = JWTManager(app)


# 用户登录，生成access_token和refresh_token
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


# 刷新access_token
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


# 用户注册
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


# 上传文件到data目录，并保存文件信息到数据库
class UploadApi(Resource):
    def post(self):
        title = request.form.get("title")
        description = request.form.get("description")
        another_title = request.form.get("anotherTitle")
        japanese_title = request.form.get("japaneseTitle")
        type = request.form.get("type")
        cover_image = request.files.get("coverImage")
        files = request.files.getlist("files")

        response = {
            "message": "Files uploaded",
            "title": title,
            "description": description,
        }

        def create_directory_if_not_exists(directory):
            if not os.path.exists(directory):
                os.makedirs(directory)

        if cover_image:
            response["cover"] = "cover!"
            directory = f"{DATA_PATH}{type}\\{title}"
            create_directory_if_not_exists(directory)
            cover_image.save(os.path.join(directory, cover_image.filename))
        else:
            response["cover"] = "No cover!"

        if files:
            response["files"] = "files!"
            for file in files:
                response["file"] = "file!"
                directory = f"{DATA_PATH}{type}\\{title}"
                create_directory_if_not_exists(directory)
                file.save(os.path.join(directory, file.filename))
        else:
            response["files"] = "No files!"

        anime = Anime(
            title=title,
            episode_count=len(files),
            description=description,
            title_another=another_title,
            title_japanese=japanese_title,
            release_date="2021-01-01",
            update_date="2021-01-01",
            view_count=0,
            download_count=0,
        )
        db.session.add(anime)
        db.session.commit()

        return response, 201


class CommentApi(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "anime_id", type=int, required=True, help="Anime ID is required"
        )
        parser.add_argument(
            "content", type=str, required=True, help="Content is required"
        )
        parser.add_argument(
            "username", type=str, required=True, help="Username is required"
        )
        args = parser.parse_args()
        anime_id = args["anime_id"]
        content = args["content"]
        username = args["username"]
        create_date = datetime.now()
        userip = request.headers.get("X-Forwarded-For", request.remote_addr)
        comment = Comment(
            anime_id=anime_id,
            content=content,
            create_date=create_date,
            username=username,
            ip=userip,
        )
        db.session.add(comment)
        db.session.commit()
        return {"message": "Comment added successfully"}, 201

    def get(self):
        anime_id = request.args.get("anime_id")
        comments = Comment.query.filter_by(anime_id=anime_id).all()
        result = [
            {
                "id": comment.id,
                "content": comment.content,
                "create_date": comment.create_date.isoformat(),
                "username": comment.username,
                "ip": comment.ip,
            }
            for comment in comments
        ]
        count = len(result)
        return {"comments": result, "count": count}


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
