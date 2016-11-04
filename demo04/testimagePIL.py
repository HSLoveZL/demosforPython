import Image
im = Image.open('/home/hongsh/Downloads/2016-11-04.jpeg')
w, h = im.size
im.thumbnail((w//2, h//2))
im.save('/home/hongsh/Downloads/modify.jpeg', 'png')
