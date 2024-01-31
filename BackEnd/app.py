from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
import settings
from settings import db
from apis import HomeApi,UserApi,AnimeApi

app = Flask(__name__)
app.config.from_object(settings)
api = Api(app)
db.init_app(app)

api.add_resource(HomeApi, '/api')
api.add_resource(AnimeApi, '/api/anime', '/api/anime/<int:anime_id>')
api.add_resource(UserApi, '/api/user')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug='true')
