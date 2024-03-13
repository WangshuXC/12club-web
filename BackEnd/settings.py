from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DIALECT = "mysql"
DRIVER = "pymysql"
USERNAME = "root"
PASSWORD = "12345678"
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "12club"
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(
    DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False

# 文件保存路径
DATA_PATH = "D:\\Codefile\\12Club\\Data\\"
