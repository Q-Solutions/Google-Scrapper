import os
from flask import Flask


scrapper = Flask(__name__)
scrapper.config['SECRET_KEY'] = 'MyKey'

basedir = os.path.abspath(os.path.dirname(__file__))
# scrapper.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
# scrapper.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

