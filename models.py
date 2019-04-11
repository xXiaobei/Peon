# encoding:utf-8
# 数据库model

from utils.functions import db


# 服务器model
class Server(db.Model):
    __tablename__ = 'servers'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    server_name = db.Column(db.VARCHAR(length=255), nullable=False)
    server_ip = db.Column(db.VARCHAR(length=255))
    database_user = db.Column(db.VARCHAR(length=100), nullable=False)
    database_pwd = db.Column(db.VARCHAR(length=100), nullable=False)
    database_port = db.Column(db.Integer, default=3306)
    domains = db.relationship("Domain", backref='server')  # 第一多关系的对象体现 backref 在关联的对象上注册 server属性


class Domain(db.Model):
    __tablename__ = 'domain'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    domain_name = db.Column(db.VARCHAR(length=255))
    update_counter = db.Column(db.Integer, nullable=False, default=5)
    category_id = db.Column(db.Integer, nullable=False)
    category_path = db.Column(db.VARCHAR(length=255), nullable=False)
    update_type = db.Column(db.Integer, default=0)  # 0 服务器更新 1 单个站点更新
    server_id = db.Column(db.Integer, db.ForeignKey('servers.id'))

    def __repr__(self):
        return '<Domain %s cid:%s cpath:%s>' % (self.domain_name, self.category_id, self.category_path)

    def __repr__(self):
        return '<Servers %s>' % self.server_name
