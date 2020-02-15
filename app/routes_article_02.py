from flask import render_template
from app import app
import json, os


@app.route('/article-02/welcome')
def article_02_welcome():
    with app.open_resource("templates/article-02/data.json", "r" ) as data_file:
        data = json.load(data_file)
    
    return render_template("article-02/welcome.html", **data)


@app.route('/article-02/chapter-02')
def article_02_chapter_01():
    return render_template("article-02/chapter-01.html")


@app.route('/article-02/resource')
def article_02_resource():
    return render_template("article-02/resource.html")