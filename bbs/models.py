# coding:utf-8

from datetime import datetime
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from . import db


class Users(db.Model):

    __tablename__ = "bbs_users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login_name = db.Column(db.String(16), nullable=False, unique=True, comment="登录的用户名")
    password_hash = db.Column(db.String(128), nullable=False)
    nickname = db.Column(db.String(16), nullable=False)
    name = db.Column(db.String(16), nullable=False)

    create_time = db.Column(db.DateTime, default=datetime.now)
    last_login_time = db.Column(db.DateTime, default=datetime.now)

    problem = db.relationship("Problem", backref="user")
    solve = db.relationship("Solve", backref="user")

    @property
    def password(self):
        raise AttributeError("这个属性只能设置，不能读取")

    @password.setter
    def password(self, value):
        self.password_hash = generate_password_hash(value)

    def check_password(self, pwd):
        return check_password_hash(self.password_hash, pwd)


class Problem(db.Model):

    __tablename__ = "bbs_problem"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.TEXT, nullable=True)
    price = db.Column(db.Integer, default=0)
    status = db.Column(db.Integer, default=0, comment="是否置顶")

    user_id = db.Column(db.Integer, db.ForeignKey("bbs_users.id"), nullable=False)

    answer = db.relationship("Solve", backref="problem")

    create_time = db.Column(db.DateTime, default=datetime.now)
    change_time = db.Column(db.DateTime, default=datetime.now)


class Solve(db.Model):

    __tablename__ = "bbs_solve"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    answer = db.Column(db.TEXT, nullable=False)

    status = db.Column(db.Integer, nullable=False, default=0)  # 0 未采纳 1 已采纳
    user_id = db.Column(db.Integer, db.ForeignKey("bbs_users.id"), nullable=False)
    problem_id = db.Column(db.Integer, db.ForeignKey("bbs_problem.id"), nullable=False)

    create_time = db.Column(db.DateTime, default=datetime.now)












