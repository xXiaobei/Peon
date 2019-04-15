# encoding:utf-8
import pymysql


# 数据库辅助类
class DB_Helper:

    def __init__(self, host, user, pwd, port, db_name, charset='utf8'):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.port = port
        self.db_name = db_name
        self.charset = charset

        try:
            self.con = pymysql.connect(host=host, user=user, password=pwd, db=db_name, charset=charset,
                                       cursorclass=pymysql.cursors.DictCursor)
        except:
            return False
        self.cur = self.con.cursor()
        return True

    # 关闭链接
    def close_connection(self):
        if self.cur and self.con:
            self.cur.close()
            self.con.close()

    # 获取当前数据库所有的用户表
    def get_customer_tables(self):
        if self.con and self.cur:
            sql_tables = 'SHOW DATABASES '
            return self.cur.execute(sql_tables)
        return None

    # 获取当前网站的栏目
    def get_archive_types(self, dbname):
        if dbname and self.con and self.cur:
            sql_types = 'SELECT * FROM %s.dede_arctype' % dbname
            return self.cur.execute(sql_types)
        return None

    # 获取网站主要配置信息
    def get_website_conf(self, dbname):
        if dbname and self.con and self.cur:
            sql_conf = "SELECT 'cfg_basehost','cfg_webname','cfg_keywords','cfg_description','cfg_beian' FROM %s.dede_sysconfig" % dbname
            return self.cur.execute(sql_conf)
        return None
