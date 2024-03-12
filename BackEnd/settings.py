from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DIALECT = "mysql"
DRIVER = "pymysql"
USERNAME = "admin"
PASSWORD = "123456"
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "12club"
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(
    DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False
