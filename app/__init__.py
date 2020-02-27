from flask import Flask

# app config
app = Flask(__name__, instance_relative_config=True)

# import routers
from app import routes_website
from app import routes_article_01
from app import routes_article_02
from app import routes_article_03

# import config
app.config.from_object('config')