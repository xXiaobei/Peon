# encoding:utf-8

from flask import Blueprint
from flask import render_template
from utils.forms import ServerForm

home_blue = Blueprint('home_blue', __name__)


@home_blue.route('/')
@home_blue.route('/index')
def index():
    return render_template('index.html', slidebar=True)


@home_blue.route('/server')
def servers():
    return render_template('list_servers.html', slidebar=False)


@home_blue.route('/serverAdd', methods=['POST', 'GET'])
def server_add():
    server_form = ServerForm()

    return render_template(
        'from_servers.html',
        slidebar=False,
        form=server_form)
