from flask import Blueprint

user_module = Blueprint(
    'user_module',
    __name__,
    url_prefix='/user'
)
# 让模块对象与文件关联起来
from app.resources.user import views

