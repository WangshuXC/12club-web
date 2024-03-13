from flask import Flask
from flask_cors import CORS
from flask_restful import Api
import settings
from settings import db
from apis import (
    HomeApi,
    UserApi,
    AnimeApi_detail,
    AnimeApi_page,
    LoginApi,
    SignupApi,
    UploadApi,
)
from flask_jwt_extended import JWTManager


app = Flask(__name__)

CORS(app, supports_credentials=True)

app.config["JWT_SECRET_KEY"] = "your_secret_key"
jwt = JWTManager(app)

app.config.from_object(settings)
api = Api(app)
db.init_app(app)

api.add_resource(UploadApi, "/api/upload", endpoint="upload")
api.add_resource(LoginApi, "/api/login", endpoint="login")
api.add_resource(SignupApi, "/api/signup", endpoint="signup")
api.add_resource(HomeApi, "/api")
api.add_resource(
    AnimeApi_detail, "/api/anime", "/api/anime/<int:anime_id>", endpoint="anime"
)
api.add_resource(
    AnimeApi_page,
    "/api/animepage",
    "/api/animepage/<int:animepage_id>",
    endpoint="anime_page",
)
api.add_resource(UserApi, "/api/user")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug="true")
