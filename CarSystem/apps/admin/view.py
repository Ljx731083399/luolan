import os

from PIL import Image
from flask import Blueprint, render_template, request

from apps.admin.models import Car
from apps.users.modles import User

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/adindex', methods=['GET', 'POST'], endpoint='adindex')
def admin_index():
    users = User.objects()
    return render_template('admin/adindex.html', users=users)


@admin_bp.route('/search', endpoint='search')
def user_msg():
    keys = request.args.get('search')
    # 使用正则表达式匹配包含keys的数据
    users = User.objects(__raw__={"$or": [{"username": {"$regex": keys}}, {"password": {"$regex": keys}}]})
    print(len(users))
    if len(users) != 0:
        return render_template('admin/adindex.html', users=users)
    else:
        return render_template('admin/adindex.html', msg='请检查输入是否有误或不存在该用户！')


@admin_bp.route('/admincar', endpoint='admincar')
def admin_car():
    cars = Car.objects()
    return render_template('admin/admincar.html', cars=cars)


@admin_bp.route('/addcar', methods=['GET', 'POST'], endpoint='addcar')
def add_car():
    if request.method == 'POST':
        brand = request.form.get('brand')
        series = request.form.get('series')
        color = request.form.get('color')
        price = request.form.get('price')
        phone = request.form.get('phone')
        getphoto = request.files['photo']
        getphoto.save('static/images/%s.jpg' % series)
        photo = 'images/%s.jpg' % series
        photo_url = 'static'
        content = request.form.get('content')
        car = Car(brand=brand, series=series, color=color, price=price, photo_url=photo_url, phone=phone, photo=photo, content=content)
        car.save()
        return render_template('admin/admincar.html')
    return render_template('admin/addcar.html')

@admin_bp.route('/goods', endpoint='goods')
def goods():
    cars = Car.objects()
    return render_template('admin/goods.html', cars=cars)
