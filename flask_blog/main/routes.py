from flask import render_template, Blueprint
from flask_blog.models import User

main = Blueprint('main', __name__)
link_names = ["home", "about", "contact", "services", "login", "register", "account", "logout"]
routes = [
    {"href": f"/{link_name.lower()}", "name": link_name.lower()} for link_name in link_names
]
print(routes)


@main.route("/")
@main.route("/home")
def home():
    return render_template('index.html', links=routes)


@main.route("/about")
def about():
    return render_template("about.html", links=routes)


@main.route("/contact")
def contact():
    return render_template("contact.html", links=routes)


@main.route("/services")
def services():
    return render_template("services.html", links=routes)
