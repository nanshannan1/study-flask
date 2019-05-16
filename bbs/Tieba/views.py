from flask import redirect, request, \
    render_template, url_for, session


from . import tie_ba
from bbs.utils.commons import login_required
from bbs.utils import operation_db
from bbs.models import Problem, Solve


@tie_ba.route("/index/<int:page>", methods=["GET"])
@tie_ba.route("/index", defaults={'page': 1}, methods=["GET"])
def index(page):

    PER_PAGE = 5
    paginate = Problem.query.paginate(page, PER_PAGE, error_out=False)

    problems = paginate.items

    return render_template("index.html", paginate=paginate, problems=problems)


@tie_ba.route("/add", methods=["POST", "GET"])
@login_required
def add():
    if request.method == "GET":
        return render_template("add.html")
    if request.method == "POST":
        data = request.form
        title = data.get("title")
        content = data.get("content")
        price = data.get("reward")
        login_name = session.get("login_name")
        if not all([title, content, price, login_name]):
            return render_template("add.html", errmsg="参数不完整")
        user = operation_db.select_user(login_name)
        if user:
            result = operation_db.add_problem(title, content, price, user.id)
            if result:
                return redirect(url_for("tie_ba.index"))
            else:
                return render_template("add.html", errrmsg="添加失败")

        else:
            return redirect(url_for('user.login'))


@tie_ba.route("/detail/<int:id>", methods=["POST", "GET"])
def detail(id):
    problem = Problem.query.get(int(id))
    solve = Solve.query.filter_by(problem_id=problem.id)
    if request.method == "GET":
        return render_template("/detail.html", problem=problem, solve=solve)
    if request.method == "POST":
        pass








