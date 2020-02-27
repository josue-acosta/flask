from flask import render_template, request, redirect
from app import app
import json


with app.open_resource("templates/article-03/data.json", "r" ) as data_file:
		data = json.load(data_file)


@app.route('/article-03/welcome')
def article_03_welcome():
	return render_template("article-03/welcome.html", **data)


@app.route('/article-03/chapter-01', methods=["GET", "POST"])
def article_03_chapter_01():
	if request.method == "POST":
		age_json = json.dumps(request.form.get("age"))

		print(type(request.form.get("age")))
		print(age_json)

		form_data = {
			"first_name" : request.form.get("first_name"),
			"last_name" : request.form.get("last_name"),
			"age" : int(request.form.get("age")),
			"day_born" : request.form.get("day_born")
		}

		with open("./app/templates/article-03/form_data.json", "w") as form_data_file:
			json.dump(form_data, form_data_file)

		return redirect(request.url)
	
	return render_template("article-03/chapter-01.html", **data)


@app.route('/article-03/resource')
def article_03_resource():
	return render_template("article-03/resource.html", **data)