from flask import session, redirect, url_for, g
import functools


# 定义的验证登录状态的装饰器
def login_required(view_func):
    # wraps函数的作用是将wrapper内层函数的属性设置为被装饰函数view_func的属性
    @functools.wraps(view_func)
    def wrapper(*args, **kwargs):
        # 判断用户的登录状态
        login_name = session.get("login_name")

        # 如果用户是登录的， 执行视图函数
        if login_name is not None:
            # 将user_id保存到g对象中，在视图函数中可以通过g对象获取保存数据
            g.login_name = login_name
            return view_func(*args, **kwargs)
        else:
            # 如果未登录，返回未登录的信息
            return redirect(url_for('user.login'))
    return wrapper