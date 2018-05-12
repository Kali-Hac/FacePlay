from django.test import TestCase
import cv2, base64
# Create your tests here.
with open("0.txt", 'r') as f:
	strs = f.read()
imgdata = base64.b64decode(strs)  # 解码
file = open('0.png', 'wb')  # 保存为0.png的图片
file.write(imgdata)
file.close()