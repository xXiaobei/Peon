# encoding:utf-8
#  主程序入口文件

from utils.init_app import create_app

#  创建工程
app = create_app()

if __name__ == '__main__':
    app.run()
