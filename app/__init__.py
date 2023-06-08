from flask import Flask
from os import path as OS_path
import sys
from flask_sqlalchemy import SQLAlchemy

baseDir = OS_path.dirname(
    OS_path.dirname(
        OS_path.abspath(__name__)
    )
)

# sys.path.insert(0, baseDir + '/common')

from app.settings.config import config_dict
from common.utils.constants import EXTRA_ENV_CONFIG


def createFlaskAPP(type):
    app = Flask(__name__)
    # 根据 type 加载配置
    config_class = config_dict[type]
    # 加载默认配置
    app.config.from_object(config_class)
    # 加载额外配置
    app.config.from_envvar(EXTRA_ENV_CONFIG, silent=True)  # silent=True 无法加载额外配置时不报错

    return app


db = SQLAlchemy()


# 注册模块
def register_module(app: Flask):
    from app.resources.user import user_module
    app.register_blueprint(user_module)


# 创建应用 和 组件初始化
def create_app(type):
    # 创建flask应用
    app = createFlaskAPP(type)
    # 组件初始化
    db.init_app(app)
    # 调用注册模块(蓝图)函数
    register_module(app)

    return app
