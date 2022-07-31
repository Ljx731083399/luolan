from bson import ObjectId
from flask import Blueprint, render_template, request, session, redirect, jsonify, url_for, g, app
from pymongo import response

from apps.admin.models import Car
from apps.users.modles import User

user_bp = Blueprint('user', __name__)
required_login_list = ['/user/index']


# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@user_bp.before_app_request
def before_request():
    print('before_app_request', request.path)
    if request.path in required_login_list:
        id = session.get('uid')
        if not id:
            return render_template('user/login.html')
        else:
            user = User.objects(id)
            g.user = user


@user_bp.route('/', endpoint='index')
def index():
    uid = request.cookies.get('uid', None)
    if uid:
        for user in User.objects(id=ObjectId(uid)):
            user = user.username
            return render_template('user/index.html', user=user)
    else:
        return render_template('user/index.html')
    return render_template('user/index.html')

@user_bp.route('/register', methods=['GET', 'POST'], endpoint='register')
def user_register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        email = request.form.get('email')
        phone = request.form.get('phone')
        if password == repassword:
            user = User()
            user.username = username
            user.password = password
            user.email = email
            user.phone = phone
            user.save()
            return redirect(url_for('user.index'))
        else:
            return render_template('user/register.html', register_msg='密码不一致')
    return render_template('user/register.html')


@user_bp.route('/delete', methods=['GET', 'POST'], endpoint='delete')
def user_delete():
    user_id = request.args.get('user_id')
    print(user_id)
    user_id = ObjectId(user_id)
    for user in User.objects:
        if user.id == user_id:
            User.delete(user)
            return 'redirect(' / ')'
        else:
            return render_template('user/adminindex.html', msg='删除失败!')


@user_bp.route('/update', methods=['POST', 'GET'], endpoint='update')
def user_center():
    if request.method == 'POST':
        uid = request.cookies.get('uid')  # 获取cookie里的uid
        print(uid)
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        email = request.form.get('email')
        phone = request.form.get('phone')
        if password == repassword:
            print('密码一致')
            for user in User.objects(id=uid):
                print(user)
                print(user.username)
                user.update(username=username, password=password, email=email, phone=phone)
                return render_template('user/update.html', up_msg='修改成功')
        else:
            return render_template('user/update.html', password_msg='密码不一致')
    return render_template('user/update.html')


@user_bp.route('/bases', endpoint='bases')
def base():
    users = User.objects()
    return render_template('bases.html', users=users)


@user_bp.route('/checkphone', methods=['POST', 'GET'], endpoint='checkphone')
def check_phone():
    get_phone = request.args.get('phone')
    print(get_phone)
    if len(User.objects(phone=get_phone)) == 0:
        return jsonify(code=200, phone_msg='号码可以注册!')
    else:
        return jsonify(code=400, phone_msg='号码已被注册!')


@user_bp.route('/login', methods=['POST', 'GET'], endpoint='login')
def login():
    if request.method == 'POST':
        get_username = request.form.get('username')
        get_password = request.form.get('password')
        repassword = request.form.get('repassword')
        use = request.form.get('use')
        if use == 'user':
            if get_password == repassword:
                User.objects(username=get_username)
                for user in User.objects(username=get_username):
                    if user.password == get_password:
                        response = redirect(url_for('user.index'))
                        response.set_cookie('uid', str(user.id), max_age=1800)
                        return response
                    else:
                        return render_template('user/login.html', password_msg='密码错误')
            else:
                return render_template('user/login.html', password_msg='密码不一致')
        else:
            if get_password == repassword:
                User.objects(username=get_username)
                for user in User.objects(username=get_username):
                    if user.password == get_password:
                        if user.is_admin == '1':
                            response = redirect(url_for('admin.adindex'))
                            response.set_cookie('uid', str(user.id), max_age=1800)
                            return response
                        else:
                            return render_template('user/login.html', password_msg='你不是管理员')
                    else:
                        return render_template('user/login.html', password_msg='密码错误')
            else:
                return render_template('user/login.html', password_msg='密码不一致')
    return render_template('user/login.html')


@user_bp.route('/logout', endpoint='logout')
def logout():
    response = redirect(url_for('user.index'))
    response.delete_cookie('uid')
    return response
