from flask import render_template, request, redirect
from app import app
import json


with app.open_resource("templates/article-03/data.json", "r" ) as data_file:
		data = json.load(data_file)

def find_group_number(birthday):
	return birthday + 100

@app.route('/article-03/welcome')
def article_03_welcome():
	return render_template("article-03/welcome.html", **data)


@app.route('/article-03/chapter-01', methods=["GET", "POST"])
def article_03_chapter_01():
	if request.method == "POST":

		group_number = find_group_number(int(request.form.get("birthday")))

		form_data = {
			"first_name": request.form.get("first_name"),
			"last_name": request.form.get("last_name"),
			"phone_number": request.form.get("phone_number"),
			"children": [
				{
					"first_name": request.form.get("first_name"),
					"last_name": request.form.get("last_name"),
					"birthday": int(request.form.get("birthday")),
					"group_number": group_number
				}
			]
		}

		with open("./app/templates/article-03/form_data.json", "w") as form_data_file:
			json.dump(form_data, form_data_file)

		return redirect(request.url)
	
	return render_template("article-03/working-form.html", **data)


@app.route('/article-03/resource')
def article_03_resource():
	return render_template("article-03/resource.html", **data)