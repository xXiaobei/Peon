from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from utils.mysqlHelper import DB_Helper

#  创建第三方插件
bt = Bootstrap()
db = SQLAlchemy()


# 初始化第三方插件
def init_exts(app):
    db.init_app(app)
    bt.init_app(app)


# 将对象转为字典
def object_to_dictionary(obj):
    if obj:
        pass


# 链接Server上的mysql库 ??
def TO_DO():
    pass
