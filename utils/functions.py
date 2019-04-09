import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from views import home_blue

#  创建第三方插件
bt = Bootstrap()
db = SQLAlchemy()

ROOTPATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
STATIC_DIR = os.path.join(ROOTPATH, 'static')
TEMPLATE_DIR = os.path.join(ROOTPATH, 'templates')


# print('s %s   t %s' % (STATIC_DIR, TEMPLATE_DIR))


#  创建工程
def create_app():
    #  创建工程对象
    app = Flask(__name__, static_folder=STATIC_DIR,
                template_folder=TEMPLATE_DIR)  # 初始化工程项目时，static 和 templates的路径都要给绝对路径

    #  配置工程相关配置项
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///peon.db'
    app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #  注册蓝图
    app.register_blueprint(home_blue, url_prefix='')
    app.register_blueprint(home_blue, url_prefix='/index')

    #  绑定第三发插件
    db.init_app(app)
    bt.init_app(app)

    return app
