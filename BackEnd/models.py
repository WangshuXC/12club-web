from settings import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)


class Anime(db.Model):
    __tablename__ = "anime"
    id = db.Column(db.Integer, primary_key=True)
    episode_count = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    title_another = db.Column(db.String(255))
    title_japanese = db.Column(db.String(255))
    description = db.Column(db.String(4095))
    isover = db.Column(db.Boolean, default=False, nullable=False)
    release_date = db.Column(db.DateTime, nullable=False)
    update_date = db.Column(db.DateTime, nullable=False)
    view_count = db.Column(db.Integer, default=0, nullable=False)
    download_count = db.Column(db.Integer, default=0, nullable=False)
    cover = db.Column(db.String(255))
