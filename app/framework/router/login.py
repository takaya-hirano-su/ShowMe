from flask import Blueprint

login_router = Blueprint("login", __name__, url_prefix="/login")


@login_router.route("/", methods=["POST"])
def login():
    return "login"
