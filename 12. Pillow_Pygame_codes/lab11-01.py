#1
from PIL import Image, ImageFilter, ImageEnhance, ImageOps
import random

#2
# 랜덤한 파일을 추출
number = random.randint(1, 99)
if number < 10 :
    number = '0' + str(number)
else :
    number = str(number)

filename = 'C:/photo/picture' + number + '.jpg'


#3
img = Image.open(filename)
img.show()
img = img.transpose(Image.FLIP_LEFT_RIGHT)
img.show()
img = img.transpose(Image.FLIP_TOP_BOTTOM)
img.show()
img = img.rotate(45, expand=True)
img.show()
img = img.filter(ImageFilter.CONTOUR)
img.show()

#4
filename = 'C:/photo/output' + number + '.jpg'
img.save(filename)
