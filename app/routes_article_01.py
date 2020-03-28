from flask import render_template
from app import app


@app.route('/article-01/welcome')
def article_01_welcome():
	return render_template("article-01/welcome.html")


@app.route('/article-01/chapter-01')
def article_01_chapter_01():
	return render_template("article-01/chapter-01.html")


@app.route('/article-01/resource')
def article_01_resource():
	return render_template("article-01/resource.html")