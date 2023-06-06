from flask import Flask
from os import path as OS_path
import sys

baseDir = OS_path.dirname(
    OS_path.abspath(__file__)
)

sys.path.insert(0, baseDir + '/common')

from app.settings.config import config_dict
from common.utils.constants import EXTRA_ENV_CONFIG


def createFlaskAPP(type):
    app = Flask(__name__)
    # 根据 type 加载配置
    config_class = config_dict[type]
    # 加载默认配置
    app.config.from_object(config_class)
    # 加载额外配置
    app.config.from_envvar(EXTRA_ENV_CONFIG)

    return app


def create_app(type):
    """创建应用 和 组件初始化"""

    # 创建flask应用
    app = createFlaskAPP(type)
    # 组件初始化

    return app