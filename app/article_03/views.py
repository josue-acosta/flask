from flask import render_template, Blueprint, request
from app import app

from app.article_03.models import *

article_03_blueprint = Blueprint("article_03", __name__, template_folder='templates')

@article_03_blueprint.route('/welcome')
def welcome():
	return render_template("/article-03/welcome.html")


@article_03_blueprint.route('/chapter-01', methods=["GET", "POST"])
def chapter_01():
	if request.method  == "POST":
		if request.files:
			upload_file(request.files["upload-form"])

	return render_template("/article-03/chapter-01.html")


@article_03_blueprint.route('/resource')
def resource():
	return render_template("/article-03/resource.html")