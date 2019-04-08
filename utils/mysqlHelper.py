# encoding:utf-8
import pymysql


# 数据库辅助类
class DB_Helper:
    
    def __init__(self, host, user, pwd, port, db_name, charset):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.port = port
        self.db_name = db_name
        self.charset = charset

        self.con = pymysql.connect(host=host, user=user, password=pwd, db=db_name, charset=charset,
                                   cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    # 关闭链接
    def close_connection(self):
        pass

    # 返回用户的列表
    def list_user(self):
        pass
