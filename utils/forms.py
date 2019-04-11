# encoding:utf-8
# 所有表单集合

from flask_wtf import FlaskForm
# 从wtforms 导入表单所用的input类型 eg StringField
from wtforms import fields
# 从 wtforms.validators 表单验证插件包 导入 需要验证的种类
from wtforms.validators import input_required, length


class ServerForm(FlaskForm):
    # render_kw 为控件的附属属性 为 字典 类型
    server_name = fields.StringField(u'服务器名', validators=[input_required(u"请填写服务器名称"), length(max=20)],
                                     render_kw={"placeholder": u"请填服务器名"})
    server_ip = fields.StringField(u'服务器IP', validators=[input_required(u"服务器IP不能为空")],
                                   render_kw={"placeholder": u"请填写服务器IP"})
    database_user = fields.StringField(u'数据库用户', validators=[input_required(u"请填写该服务器数据库的用户")],
                                       render_kw={"placeholder": u"请填数据库用户"})
    database_pwd = fields.PasswordField(u'数据库密码', validators=[input_required(u"请填写该服务器数据库的密码")],
                                        render_kw={"placeholder": u"请填写数据库密码"})
    database_port = fields.StringField(u'数据库端口', validators=[input_required(u"请填写该服务器数据库的用户")],
                                       render_kw={"placeholder": u"请填写数据库的端口，默认3306"})
