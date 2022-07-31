import settings
from flask import Flask

from apps.admin.view import admin_bp
from apps.users.view import user_bp
from ext import db, bootstrap


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(settings.DevelopmentConfig)  # 配置文件
    db.init_app(app=app)  # 将db对象与app进行关联
    bootstrap.init_app(app=app)  # 将bootstrap对象与app进行关联
    app.register_blueprint(user_bp)  # 注册蓝图
    app.register_blueprint(admin_bp)  # 注册蓝图
    # print(app.url_map)
    return app
