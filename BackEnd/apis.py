from flask import request
from flask_restful import Resource
from models import User,Anime
from settings import db
import math

class HomeApi(Resource):
    def get(self):
        return {'message': 'Hello, World!'}

class AnimeApi(Resource):
    def get(self, anime_id=None, animepage_id=None):
        if anime_id:
            # 根据 ID 获取特定的动漫信息
            anime = Anime.query.get(anime_id)
            if anime:
                return {
                    'id': anime.id,
                    'title': anime.title,
                    'title_another': anime.title_another,
                    'title_japanese': anime.title_japanese,
                    'description': anime.description,
                    'release_date': anime.release_date.isoformat(),
                    'update_date': anime.update_date.isoformat(),
                    'view_count': anime.view_count,
                    'download_count': anime.download_count
                }
            else:
                return {'message': 'Anime not found'}, 404
        elif animepage_id:
            # 计算offset值
            items_per_page = 20
            offset = (int(animepage_id) - 1) * items_per_page
            # 查询指定范围内的动漫数据
            anime_page_list = Anime.query.offset(offset).limit(items_per_page).all()
            anime_count = Anime.query.count()
            total_page=math.ceil(anime_count/items_per_page)
            # 将查询结果转换成字典列表
            results = [{
                'id': anime.id,
                'title': anime.title,
                'cover':anime.cover,
            } for anime in anime_page_list]
            result={'total_page':total_page,'results':results}
            return result,200
        else:
            # 返回表内所有的动漫信息
            anime_list = Anime.query.all()
            return [
                {
                    'id': anime.id,
                    'title': anime.title,
                    'title_another': anime.title_another,
                    'title_japanese': anime.title_japanese,
                    'description': anime.description,
                    'release_date': anime.release_date.isoformat(),
                    'update_date': anime.update_date.isoformat(),
                    'view_count': anime.view_count,
                    'download_count': anime.download_count
                } for anime in anime_list
            ]

    def post(self):
        # 创建新的动漫信息
        data = request.json
        anime = Anime(
            title=data['title'],
            description=data['description'],
            release_date=data['release_date'],
            update_date=data.get('update_date'),
            view_count=data.get('view_count', 0),
            download_count=data.get('download_count', 0)
        )
        db.session.add(anime)
        db.session.commit()
        return {'message': 'Anime created successfully'}, 201

    def put(self, anime_id):
        # 更新动漫信息
        anime = Anime.query.get(anime_id)
        if anime:
            data = request.json
            anime.title = data.get('title', anime.title)
            anime.description = data.get('description', anime.description)
            anime.release_date = data.get('release_date', anime.release_date)
            anime.update_date = data.get('update_date', anime.update_date)
            anime.view_count = data.get('view_count', anime.view_count)
            anime.download_count = data.get('download_count', anime.download_count)
            db.session.commit()
            return {'message': 'Anime updated successfully'}
        else:
            return {'message': 'Anime not found'}, 404

    def delete(self, anime_id):
        # 删除动漫信息
        anime = Anime.query.get(anime_id)
        if anime:
            db.session.delete(anime)
            db.session.commit()
            return {'message': 'Anime deleted successfully'}
        else:
            return {'message': 'Anime not found'}, 404

class UserApi(Resource):
    def get(self):
        users = db.session.query(User).all()
        result = [{'id': user.id, 'name': user.name} for user in users]
        return {'users': result}