from flask import Flask
from views import home_blue
from flask_bootstrap import Bootstrap

app = Flask(__name__)

# 第三方插件注册
bootstrap = Bootstrap(app)

# 注册蓝图
app.register_blueprint(home_blue, prefix='/home')

if __name__ == '__main__':
    app.run(debug=True)
