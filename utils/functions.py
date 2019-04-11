from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

#  创建第三方插件
bt = Bootstrap()
db = SQLAlchemy()


# 初始化第三方插件
def init_exts(app):
    db.init_app(app)
    bt.init_app(app)
