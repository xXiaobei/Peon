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
    logs = db.relationship('PublishLog', backref='server')
    publishs = db.relationship('Publish',backref='server')
    
    def __repr__(self):
        return '<Servers %s>' % self.server_name


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

# 服务器发布配置
class Publish(db.Model):
    __tablename__ = 'publish'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    database_name = db.Column(db.VARCHAR(length=255))    # 数据库名 （单例发布，数据库名必须填写）
    id_types = db.Column(db.VARCHAR(length=100),nullable=False)    # 栏目id id_types （栏目id，允许多个id，每个id用英文逗号分隔）
    data_file_path = db.Column(db.VARCHAR(length=255))# 栏目发布文件数据目录 data_file_path （火车头采集的txt地址）
    data_url_path = db.Column(db.VARCHAR())    # 栏目发布url地址 data_url_path （数据接口地址）
    arc_number_min = db.Column(db.Integer) # 栏目文章发布最少多少篇
    arc_number_max = db.Column(db.Integer) # 栏目文章发布最多多少篇
    is_keywords = db.Column(db.Integer) # 是否启用关键词替换
    is_filter = db.Column(db.Integer) # 是否启用过滤功能（需过滤的词从过滤表中拉取）
    is_resolve = db.Column(db.Integer) # 是否启用分词功能
    is_type_top = db.Column(db.Integer) # 是否发布顶级栏目
    is_index_page = db.Column(db.Integer) # 是否生存静态首页
    is_type_page = db.Column(db.Integer) # 是否生成栏目页
    is_page_all = db.Column(db.Integer) # 是否生存所有文章静态页
    is_page_curent = db.Column(db.Integer) # 是否生成本次发布的文章的静态页
    server_id = db.Column(db.Integer,db.ForeignKey('servers.id'))

    def __repr__(self):
        return '<Publish id: %s>' % self.id



# 服务器发布日志
class PublishLog(db.Model):
    __tablename__ = 'publish_log'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    logger_date = db.Column(db.DateTime, nullable=False)
    logger_success = db.Column(db.Text)
    logger_error = db.Column(db.Text)
    server_id = db.Column(db.Integer, db.ForeignKey('servers.id'))

    def __repr__(self):
        return '<Logger id: %s date: %s>' % (self.id, self.logger_date)
