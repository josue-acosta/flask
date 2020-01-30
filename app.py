from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome_page():
    return render_template("article-01/welcome.html", title="Welcome")

@app.route('/chapter-01')
def chapter_01():
    return render_template("article-01/chapter-01.html", title="Chapter 01")

@app.route('/appendix')
def appendix_page():
    return render_template("article-01/appendix.html", title="Appendix")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("article-01/404.html", title="Page Not Found"), 404

if __name__ == '__main__':
    app.run()