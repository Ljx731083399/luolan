import re

from PIL import Image
import os.path

source = 'static//RS6.JPG'
size = int(os.path.getsize(source) / 1024)
print("原始图片大小为：%d kb" % size)
im = Image.open(source)
width, height = im.size
print(width, height)
dest = im.resize((200, 200), Image.ANTIALIAS)  # 第一次压缩
# dest.save('templates/car/image/new.jpg', quality=80)  # 第二次压缩为80%
dest.save('static//RS6.png')
size = int(os.path.getsize('static/images/RS6.png') / 1024)
print("压缩图片大小为：%d kb" % size)
