from flask import Flask

# app config
app = Flask(__name__)
app.config.from_object("configuration.DevelopmentConfig")

# import routers
from app import routes_website
from app import routes_article_02

# register blueprints
from app.article_01.views import article_01_blueprint
app.register_blueprint(article_01_blueprint, url_prefix='/article-01')
