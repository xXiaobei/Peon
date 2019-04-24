# encoding:utf-8
import pymysql
import json
from functions import arc_publish_conf

# mysql 数据库配置
mysql_config = {
    "host":"",
    "port":3306,
    "user":"",
    "password":"",
    "database":"",
    "charset":"utf-8"
}


# 使用with简化资源管理 with 知识点？
# 根据配置文件生成对应的mysql持久会话
class mysql_adapter():
    def __init__(self):
        try:
            self.db_con = pymysql.Connect(**mysql_config)
            self.db_cur = self.db_con.cursor(pymysql.cursors.DictCursor)
        except expression as identifier:
            print("mysql db init error!")
    
    def __enter__(self):
        return self.db_cur
        
    def __exit__(self):
        self.db_cur.close()
        self.db_con.close()

# 设置当前数据库的配置信息
def set_mysql_config(db_conf):
    if db_conf:
        if db_conf["host"]:
            mysql_config["host"] = db_conf["host"]
        if db_conf["port"]:
            mysql_config["port"] = db_conf["port"]
        if db_conf["user"]:
            mysql_config["user"] = db_conf["user"]
        if db_conf["password"]:
            mysql_config["password"] = db_conf["password"]
        if db_conf["database"]:
            mysql_config["database"] = db_conf["database"]
        if db_conf["charset"]:
            mysql_config["charset"] = db_conf["charset"]

# 获取当前数据库汇总所有的数据库名
def get_db_names():
    with(mysql_adapter() as db):
        sql_db_name = 'SELECT DATABASES'
        db.execute(sql_db_name)
        return json.dumps(db.fetchall())
    return json.dumps([])

# 获取当前站点相关信息
def get_site_info():
    with(mysql_adapter() as db):
        list_site_info = []
        sql_arc_conf = 'SELECT aid,varname,value FROM dede_sysconfig WHERE varname IN ('cfg_description','cfg_keywords','cfg_webname','cfg_basehost');'
        sql_arc_type = 'SELECT id,reid,topid,typename,channeltype FROM dede_arctype;'
        db.execute(sql_arc_conf)
        list_site_info['arc_conf'] = db.fetchall()
        db.execute(sql_arc_type)
        list_site_info['arc_type'] = db.fetchall()
        return json.dumps(list_site_info)
    return json.dumps([])    