from flask import render_template
from flask import request, session
from flask import redirect, url_for

from . import user
from bbs.utils import operation_db


@user.route("/head", methods=["GET"])
def head():
    return render_template("/head.html")


@user.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "GET":
        return render_template("/register.html")
    if request.method == "POST":
        data = request.form
        login_name = data.get("userName")
        pwd = data.get("pass")
        check_pwd = data.get("repass")

        name = data.get("name")
        nickname = data.get("username")
        print(login_name, pwd, check_pwd, name, nickname)

        if not all([login_name, pwd, check_pwd, name, nickname]):
            return render_template("/register.html", errmsg="参数不完整")
        if pwd != check_pwd:
            return render_template("/register.html", errmsg="两次密码不一致")
        if operation_db.select_user(login_name):
            return render_template("/register.html", errmsg="登录名已经存在")
        success = operation_db.add_user(login_name, pwd, nickname, name)
        print(success)
        if success:
            return redirect(url_for('user.login'))
        else:
            return render_template("/register.html", errmsg="注册失败")


@user.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("/login.html")
    if request.method == "POST":
        data = request.form
        login_name = data.get("userName")
        pwd = data.get("pass")
        if not all([login_name, pwd]):
            return render_template("/login.html", errmsg="参数不完整")
        user = operation_db.select_user(login_name)
        if not user:
            return render_template("/login.html", errmsg="用户不存在")
        if user.check_password(pwd):
            # 登录成功保存登录状态，session中
            session['login_name'] = login_name
            return redirect(url_for('tie_ba.index'))
        else:
            return render_template("/login.html", errmsg="密码错误")



