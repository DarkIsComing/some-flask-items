from  flask import Blueprint
# 定义蓝本
main = Blueprint('main', __name__)

from . import index, errors