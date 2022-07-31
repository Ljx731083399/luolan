from datetime import datetime

from ext import db


class User(db.Document):
    username = db.StringField()
    password = db.StringField()
    email = db.StringField()
    phone = db.StringField()
    is_admin = db.StringField()  # 是否给管理权限
    registertime = db.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.username


class Buycar(db.Document):
    name = db.StringField()  # 用户名
    brand = db.StringField()  # 品牌
    series = db.StringField()  # 车型
    color = db.StringField()  # 颜色
    photo = db.StringField()  # 图片
    price = db.StringField()  # 价格

    def __str__(self):
        return self.name
