from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

#  创建第三方插件
bt = Bootstrap()
db = SQLAlchemy()

# 文章發布相关配置
class arc_publish_conf():
    def __init__(self,
        _isTops=False,
        _arcNumMin=5,
        _arcNumMax=10,
        _isKeywords=False,
        _isFilter=False,
        _isResolve=False,
        _isIndex=True,
        _isType=True,
        _isArchvies=False,
        _isCurArchives=True):
        self.isTops = _isTops # 是否发布顶级栏目
        self.arcNumMin = _arcNumMin # 栏目发布文章最小数目
        self.arcNumMax = _arcNumMax # 栏目发布文章最大书目
        self.isKeywords = _isKeywords # 是否启用关键词替换功能
        self.isFilter = _isFilter # 是否启用文章过滤功能（从数据库中获取需过滤的关键词）
        self.isResolve = _isResolve # 是否启用分词功能
        self.isIndex = _isIndex # 发布完车后是否生成首页
        self.isType = _isType # 发布完成后是否生成栏目页
        self.isArchives = _isArchvies # 是否生成所有的内容页
        self.isCurArchives = _isCurArchives # 是否生成当前发布的文档


# 初始化第三方插件
def init_exts(app):
    db.init_app(app)
    bt.init_app(app)

