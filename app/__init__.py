from flask import Flask

# app config
app = Flask(__name__)

# import routers
from app import routes_website
from app import routes_article_01
from app import routes_article_02
from app import routes_article_03