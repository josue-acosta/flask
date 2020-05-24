from flask import Flask

# app config
app = Flask(__name__)
app.config.from_object("configuration.DevelopmentConfig")

# import routers
from app import routes_website

# register blueprints
from app.article_01.views import article_01_blueprint
from app.article_02.views import article_02_blueprint
from app.article_03.views import article_03_blueprint

app.register_blueprint(article_01_blueprint, url_prefix='/article-01')
app.register_blueprint(article_02_blueprint, url_prefix='/article-02')
app.register_blueprint(article_03_blueprint, url_prefix='/article-03')