import json
from flask import Blueprint, render_template, request, redirect


article_02_blueprint = Blueprint("article_02", __name__, template_folder='templates')


with article_02_blueprint.open_resource("./templates/data.json", "r" ) as data_file:
		data = json.load(data_file)


@article_02_blueprint.route('/welcome')
def welcome():
	return render_template("welcome.html", **data)


@article_02_blueprint.route('/chapter-01')
def chapter_01():
	return render_template("chapter-01.html", **data)


@article_02_blueprint.route('/resource', methods=["GET", "POST"])
def resource():

	if request.method == "POST":
		first_name = request.form.get("first_name")
		last_name = request.form.get("last_name")

		with open("./templates/form_data.json", "w") as form_data_file:
			form_data_file.write(first_name + "\n")
			form_data_file.write(last_name + "\n")

		return redirect(request.url)

	return render_template("resource.html", **data)