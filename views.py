# encoding:utf-8

from flask import Blueprint
from flask import render_template

home_blue = Blueprint('home_blue', __name__)


@home_blue.route('/')
@home_blue.route('/index')
def index():
    return render_template('index.html')
