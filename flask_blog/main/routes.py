from flask import render_template, Blueprint
from flask_blog.models import User

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template('index.html')


@main.route("/about")
def about():
    return render_template("about.html")


@main.route("/contact")
def contact():
    return render_template("contact.html")


@main.route("/services")
def services():
    return render_template("services.html")
