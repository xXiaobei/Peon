# encoding:utf-8
# 工程脚本管理

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from utils.functions import create_app, db

app = create_app()
migrate = Migrate(app, db)  # 数据库迁移工具ma

manager = Manager(app)  # 脚本管理工具
manager.add_command('db', MigrateCommand)  # 添加数据库迁移脚本命令到 脚本管理器中

if __name__ == '__main__':
    manager.run()
