from flask import render_template
from app import app


@app.route('/')
def index():
	return render_template("website/index.html")


@app.route('/appendix')
def appendix():
	return render_template("website/appendix.html")


@app.errorhandler(404)
def page_not_found(error):
	return render_template("website/404.html", title="Page Not Found"), 404