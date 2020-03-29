from flask import render_template, Blueprint


article_01_blueprint = Blueprint("article_01", __name__, template_folder='templates')


@article_01_blueprint.route('/welcome')
def welcome():
	return render_template("article_01/welcome.html")


@article_01_blueprint.route('/chapter-01')
def chapter_01():
	return render_template("article_01/chapter-01.html")


@article_01_blueprint.route('/resource')
def resource():
	return render_template("article_01/resource.html")