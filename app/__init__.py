from flask import Flask

# app config
app = Flask(__name__, instance_relative_config=True)

# import routers
from app import routes_website
from app import routes_article_01

# import config
app.config.from_object('config')