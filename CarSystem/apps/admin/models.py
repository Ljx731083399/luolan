from ext import db



# 车库
class Car(db.Document):
    brand = db.StringField()  # 品牌
    series = db.StringField()  # 车型
    color = db.StringField()  # 颜色
    photo_url = db.StringField()  # 图片
    photo = db.StringField()  # 图片
    price = db.StringField()  # 价格
    phone = db.StringField()  # 售后
    content = db.StringField()  # 描述
    daddress = db.StringField()  # 发货地址

    def __str__(self):
        return self.brand


# 订单管理
class Order(db.Document):
    buyname = db.StringField()  # 购买用户
    raddress = db.StringField()  # 收货地址
    brand = db.StringField()  # 品牌
    series = db.StringField()  # 车型
    color = db.StringField()  # 颜色
    photo = db.StringField()  # 图片
    price = db.StringField()  # 价格

    def __str__(self):
        return self.buyname
