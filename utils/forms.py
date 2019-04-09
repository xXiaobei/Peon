# encoding:utf-8
# 所有表单集合

from flask_wtf import FlaskForm
# 从wtforms 导入表单所用的input类型 eg StringField
from wtforms import fields
# 从 wtforms.validators 表单验证插件包 导入 需要验证的种类
from wtforms.validators import input_required, length


class ServerForm(FlaskForm):
    server_name = fields.StringField('server_name', validators=[input_required(), length(max=20)])
    database_user = fields.StringField('database_user', validators=[input_required()])
    database_pwd = fields.PasswordField('database_pwd', validators=[input_required()])
    database_port = fields.StringField('database_port', validators=[input_required()])
