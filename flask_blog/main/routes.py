from flask import render_template, Blueprint
from flask_blog.models import User

main = Blueprint('main', __name__)
link_names = ["home", "login", "register", "account", "logout", "allpost", "create_post", "user_posts"]
link_href = {
    "create_post": "post/new",
    "user_posts": "user/"
}
# "about", "contact", "services"
routes = [
    {"href": f"/{link_name.lower() if link_href.get(link_name.lower()) is None else link_href[link_name.lower()]}",
     "name": link_name.lower().replace("_", " ")} for link_name in link_names
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
