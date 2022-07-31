from bson import ObjectId

from apps.admin.models import Car
from apps.users.modles import User

car = Car()
brand = '奥迪'  # 品牌
series = '2022款RS6'  # 车型
color = '星空灰'  # 颜色
photo_url = 'static'  # 图片
photo = 'images/RS6.png'  # 图片
price = '144.38万'  # 价格
phone = '3351-754643'  # 售后
content = '2022款 RS6 4.0T Avant'  # 描述
daddress = '来宾'  # 发货地址
car.brand=brand
car.series=series
car.color=color
car.photo_url=photo_url
car.photo=photo
car.price=price
car.phone=phone
car.content=content
car.daddress=daddress
car.save()

# car = Car.objects(brand='奥迪').first()
# photo = car.photo.read()
# content_type = car.photo.content_type
# print(type(photo))
# print(type(content_type))
# print(content_type)
# admin = Admin()
# name = 'admin'
# password = 'admin'
# admin.admin = name
# admin.admin_password = password
# admin.save()
# #
# user = User()
# username = 'admin'
# password = 'admin'
# email = 'admin888@163.com'
# phone = '18376441839'
# is_admin = '1'
# user.username=username
# user.password=password
# user.email=email
# user.phone=phone
# user.is_admin=is_admin
# user.save()
# user.username=username
# user.password=password
# user.email=email
# user.phone=phone
# user.save()
# bttf = User.objects(password='4444').get_or_404()
# bttf = User.objects(id="6237207f94cae9a432f32520")  # 通过id查找数据
# print(len(bttf))
# for user in User.objects:
#     print(user.id)
#     print(type(str(user.id)))
#     print(user.username)
#     # 打印张三张四
# print(len(bttf))
# print(type("62357e1813ce3738ee9945d5"))



# content_type = marmot.photo.content_type
# print(photo)
# print(content_type)

# with open('templates/car/image/1.png', 'rb') as car:
#     marmot.photo.put(car, content_type='image/png')
# marmot.save()
# marmot = Car.objects(genus='Marmota').first()
# photo = marmot.photo.read()
# outf = open('/static//%d.png' % 10, 'wb')
# outf.write(photo)  # 存储图片
# outf.close()
# ross = CarUser(email='ross@example.com')
# ross.first_name = 'Ross'
# ross.last_name = 'Lawley'
# ross.save()
# post1 = TextPost(title='Fun with MongoEngine', author='john')
# post1.content = 'Took a look at MongoEngine today, looks pretty cool.'
# post1.tags = ['mongodb', 'mongoengine']
# post1.save()
#
# post2 = LinkPost(title='MongoEngine Documentation', author='ross')
# post2.link_url = 'http://docs.mongoengine.com/'
# post2.tags = ['mongoengine']
# post2.save()
# for post in Post.objects:
#     print("遍历post表中的帖子标题并输出：", post.title)
#输出:Fun with MongoEngine
# MongoEngine Documentation
# for post in TextPost.objects:
#     print(post.content)
# for post in Post.objects:
#     print(post.title)
#     print('=' * len(post.title))
#
#     if isinstance(post, TextPost):
#         print(post.content)
#
#     if isinstance(post, LinkPost):
#         print('Link: {}'.format(post.link_url))
# for post in Post.objects(tags='mongodb'):
#     print(post.title)
# num_posts = Post.objects(tags='mongodb').count()
# print('Found {} posts with tag "mongodb"'.format(num_posts))