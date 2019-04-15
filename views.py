# encoding:utf-8

from flask import Blueprint, request, flash, jsonify
from flask import render_template
from werkzeug.security import generate_password_hash, check_password_hash
from utils.forms import ServerForm
from utils.functions import db
from models import Server, Domain

home_blue = Blueprint('home_blue', __name__)


# db.Session() 为 sessionmaker 会话工厂
# db.session() 是 sessionmaker 产生的一个 线程安全（同一个线程中使用同一个session会话） 的会话对象


@home_blue.route('/')
@home_blue.route('/index')
def index():
    return render_template('index.html')


@home_blue.route('/server')
def servers():
    return render_template('list_servers.html')


@home_blue.route('/serverAdd', methods=['POST', 'GET'])
def server_add():
    server_form = ServerForm()

    if request.method == 'POST' and server_form.validate():
        server = Server()

        server.server_ip = server_form.server_ip.data
        server.server_name = server_form.server_name.data
        server.database_port = server_form.database_port.data
        server.database_user = server_form.database_user.data

        # 密码hash加密
        server.database_pwd = generate_password_hash(server_form.database_pwd.data,
                                                     method='pbkdf2:sha1',
                                                     salt_length=8)
        # 添加对象到当前会话中
        db.session.add(server)
        # 提交当前会话中的对象
        db.session.commit()

        flash(u'服务器 %s 创建成功！' % server_form.server_name.data, category='success')

    return render_template(
        'from_servers.html',
        slidebar=False,
        form=server_form)


@home_blue.route('/publish', methods=['GET', 'POST'])
def arc_publish():
    server_id = request.args.get("server_id") or -1
    if server_id != -1:
        server = Server.query.all()




        return jsonify({"a": 1, "b": 2})
    return jsonify()
