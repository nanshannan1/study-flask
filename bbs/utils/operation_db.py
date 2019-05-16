from bbs import models
from bbs import db

from flask import current_app


def select_user(login_name):
    try:
        user = models.Users.query.filter_by(login_name=login_name).first()
        return user
    except Exception as e:
        current_app.logger.error(e)
        return False


def add_user(login_name, password, nickname, name):
    try:
        user = models.Users(login_name=login_name, nickname=nickname, name=name)
        user.password = password
        db.session.add(user)
        db.session.commit()
        return True
    except Exception as e:
        current_app.logger.error(e)
        return False


def add_problem(title, content, price, user_id):
    try:
        problem = models.Problem(title=title, content=content, price=price, user_id=user_id)
        db.session.add(problem)
        db.session.commit()
        return True
    except Exception as e:
        current_app.logger.error(e)
        return False

