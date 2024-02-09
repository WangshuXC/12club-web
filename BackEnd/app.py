from flask import Flask
from flask_cors import CORS
from flask_restful import Api
import settings
from settings import db
from apis import HomeApi,UserApi,AnimeApi

app = Flask(__name__)
CORS(app)
app.config.from_object(settings)
api = Api(app)
db.init_app(app)

api.add_resource(HomeApi, '/api')
api.add_resource(AnimeApi, '/api/anime', '/api/anime/<int:anime_id>', endpoint='anime')
api.add_resource(AnimeApi, '/api/animepage', '/api/animepage/<int:animepage_id>', endpoint='anime_page')
api.add_resource(UserApi, '/api/user')


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug='true')
