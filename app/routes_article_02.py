from flask import render_template, request, redirect
from app import app
import json

with app.open_resource("templates/article-02/data.json", "r" ) as data_file:
        data = json.load(data_file)

@app.route('/article-02/welcome')
def article_02_welcome():
    return render_template("article-02/welcome.html", **data)


@app.route('/article-02/chapter-01')
def article_02_chapter_01():
    return render_template("article-02/chapter-01.html", **data)


@app.route('/article-02/resource', methods=["GET", "POST"])
def article_02_resource():

    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")

        with open("./app/templates/article-02/form_data.json", "w") as form_data_file:
            form_data_file.write(first_name + "\n")
            form_data_file.write(last_name + "\n")

        return redirect(request.url)

    return render_template("article-02/resource.html", **data)