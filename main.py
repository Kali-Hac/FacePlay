#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
☆*°☆*°(∩^o^)~━━  2018/5/5 15:06        
      (ˉ▽￣～) ~~ 一捆好葱 (*˙︶˙*)☆*°
      Fuction：        √ ━━━━━☆*°☆*°
"""
import torch
from torch.autograd import Variable
import cv2
import argparse
import numpy as np
from matlab_cp2tform import get_similarity_transform_for_cv2
import net_sphere
from mtcnn.mtcnn import MTCNN
import os, base64, datetime
path = 'model'
detector = MTCNN()
net = getattr(net_sphere, 'sphere20a')()
net.load_state_dict(torch.load(path + '/sphere20a_20171020.pth'))
net.eval()
net.feature = True


def generate_landmark(path):
	img = cv2.imread(path)
	tmp = detector.detect_faces(img)
	if len(tmp) == 0:
		print('no face')
		return [], []
	else:
		box = tmp[0]['box']
		tmp = tmp[0]['keypoints']
		landmark = []
		for t in list(tmp.items()):
			for tt in t[1]:
				landmark.append(tt)
		return landmark, box


def alignment(src_img, src_pts):
	ref_pts = [[30.2946, 51.6963], [65.5318, 51.5014],
	           [48.0252, 71.7366], [33.5493, 92.3655], [62.7299, 92.2041]]
	crop_size = (96, 112)
	src_pts = np.array(src_pts).reshape(5, 2)

	s = np.array(src_pts).astype(np.float32)
	r = np.array(ref_pts).astype(np.float32)

	tfm = get_similarity_transform_for_cv2(s, r)
	face_img = cv2.warpAffine(src_img, tfm, crop_size)
	return face_img

# imglist存放拍照的图+原来文件夹里所有存的人脸，img_name是对应过的人名，比imglist长度少1
def tell(imglist,img_name,thd=0.3085):
	img = np.vstack(imglist)
	img = Variable(torch.from_numpy(img).float(), volatile=True)
	output = net(img)
	f = output.data
	f1 = f[0]
	# torch_data = torch.from_numpy(np_data)

	# 保存向量来匹对的方法不适用
	# tensor2array = f[1:, ].numpy()
	# np.save('face_data.npy', tensor2array)
	# np.save('face_name.npy', img_name)

	for i in range(1, len(imglist)):
		# f1, f2 = f[0], f[2]
		f2 = f[i]
		cosdistance = f1.dot(f2) / (f1.norm() * f2.norm() + 1e-5)
		if (cosdistance > thd):
			print("### 人脸验证通过：%s" % img_name[i-1])
			return img_name[i-1]
		# print("### 未能识别出该人脸")
	return False

# 利用已有的人脸向量数据进行匹配,速度提升 (暂不用)
def tell_with_already(origin_img, thd=0.3085):
	landmark, _ = generate_landmark(origin_img)
	img = alignment(cv2.imread(origin_img), landmark)
	# 关键
	img = img.transpose(2, 0, 1).reshape((1, 3, 112, 96))
	img = (img - 127.5) / 128.0
	# img = img.transpose(2, 0, 1).reshape((1, 3, 112, 96))
	# img = (img - 127.5) / 128.0
	face_vec = np.load('face_data.npy')
	f = torch.from_numpy(face_vec)
	img_name = np.load('face_name.npy')
	img = np.vstack([img])
	# change
	img = Variable(torch.from_numpy(img).float(), volatile=True)
	output = net(img)
	f1 = output.data[0]

	# ftt = f1.numpy()
	# ftt = np.reshape(ftt, [1, 512])
	# temp = np.zeros(shape=(len(f), 1))
	# print(temp.shape)
	# ftt = ftt + temp
	# ftt = torch.from_numpy(ftt)
	# cos = torch.nn.CosineSimilarity(eps=1e-6)
	# ftt = ftt.double()
	# f = f.double()
	# cosdistance = cos(ftt, f)
	# print(torch.max(cosdistance, -1, True))
	# max_cosdistance = torch.max(cosdistance, -1, True)[1].data
	# if (max_cosdistance > thd):
	# 	print("### 人脸验证通过：%s" % img_name[max_cosdistance])
	# 	return img_name[max_cosdistance]

	# print(cosdistance)
	# print(torch.max(cosdistance))
	# 不使用遍历模式，而使用矩阵运算模式
	# f = f.float()
	for i in range(len(f)):
		# f1, f2 = f[0], f[2]
		f2 = f[i]
		cosdistance = f1.dot(f2) / (f1.norm() * f2.norm() + 1e-5)
		# print(cosdistance)
		if (cosdistance > thd):
			print(cosdistance)
			print("### 人脸验证通过：%s" % img_name[i - 1])
			# return img_name[i-1]
		# print("### 未能识别出该人脸")
	return False

# 添加与已存的人脸进行匹配的模式
def identfiy_all(origin_img):
	# 向量存储方法暂时不用
	# if os.path.exists('face_data.npy') and os.path.exists('face_name.npy'):
	# 	now = datetime.datetime.now()
	# 	if tell_with_already(origin_img):
	# 		end = datetime.datetime.now()
	# 		print(str(end - now))
	# 		return True
	# 	else:
	# 		end = datetime.datetime.now()
	# 		print(str(end - now))
	# 		return False

	now = datetime.datetime.now()
	if os.path.exists('face_name.npy'):
		all_faces_dir = np.load('face_name.npy')
	else:
		all_faces_dir = []
		for basedir, _, filenames in os.walk('FACEs'):
			if len(filenames) != 0:
				all_faces_dir.append('./' + basedir + '/' + str(filenames[0]))
				# if test_face(origin_img, srcimg='./' + basedir + '/' + str(filenames[0])):
				# 	print("### 人脸验证通过，用户为：")
				# 	return basedir.split('\\')[1]
				# else:
				# 	print("### 未能识别出该人脸，该图片名字为：%s" % basedir.split('\\')[1])
		np.save('face_name.npy', all_faces_dir)
	# else:
	result = test_face(origin_img, all_faces_dir)
	if result:
		end = datetime.datetime.now()
		print(str(end - now))
		return result
	else:
		end = datetime.datetime.now()
		print(str(end - now))
		return False

def test(srcimg='./face/me.jpg'):
	##############img1###################
	srcimg = srcimg
	landmark, _ = generate_landmark(srcimg)
	img1 = alignment(cv2.imread(srcimg), landmark)
	##############img2###################
	# cap = cv2.VideoCapture(0)
	# while (1):
	# 	# get a frame
	# 	ret, frame = cap.read()
	# 	# show a frame
	# 	cv2.imwrite('tmp.png', frame)
	# 	landmark, box = generate_landmark('tmp.png')
	# 	if len(landmark) == 0:
	# 		cv2.imshow("capture", frame)
	# 		continue
	# 	for i in range(5):
	# 		cv2.circle(frame, (landmark[i * 2], landmark[i * 2 + 1]), 1, (0, 255, 0), -1)
	# 	cv2.rectangle(frame, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]), (0, 255, 0), 1)
	# 	cv2.imshow("capture", frame)
	# 	if cv2.waitKey(1) & 0xFF == ord('q'):
	# 		cv2.imwrite("eval.png", frame)
	# 		break
	# cap.release()
	# cv2.destroyAllWindows()
	evalimg = '好葱.png'
	landmark, _ = generate_landmark(evalimg)
	img2 = alignment(cv2.imread(evalimg), landmark)
	#####################################
	imglist1 = [img1, cv2.flip(img1, 1), img2, cv2.flip(img2, 1)]
	for i in range(len(imglist1)):
		imglist1[i] = imglist1[i].transpose(2, 0, 1).reshape((1, 3, 112, 96))
		imglist1[i] = (imglist1[i] - 127.5) / 128.0

	if (tell(imglist1)):
		print(111)
		return True
	else:
		return False

# origin_image是待测试图片，srcimg是被匹配的图片(数据库里)
def test_face(origin_img, srcimg_dir):
	try:
		landmark, _ = generate_landmark(origin_img)
		img = alignment(cv2.imread(origin_img), landmark)
	# imglist1 = [img1, cv2.flip(img1, 1), img2, cv2.flip(img2, 1)]
		imglist1 = [img]
	except:
		return False
	img_name = []
	for srcimg in srcimg_dir:
		try:
			landmark, _ = generate_landmark(srcimg)
			img1 = alignment(cv2.imread(srcimg), landmark)
			imglist1.append(img1)
			img_name.append(srcimg.split('/')[2])
		except:
			pass
		# imglist1.append(cv2.flip(img1, 1))
	# print(len(imglist1))
	for i in range(len(imglist1)):
		imglist1[i] = imglist1[i].transpose(2, 0, 1).reshape((1, 3, 112, 96))
		imglist1[i] = (imglist1[i] - 127.5) / 128.0
	if (tell(imglist1, img_name)):
		return True
	else:
		return False

def get_face(base64_data):
	imgData = base64.b64decode(base64_data)
	nparr = np.fromstring(imgData, np.uint8)
	img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
	cv2.imwrite('temp_face.png', img_np)
	srcimg = cv2.imread('temp_face.png')
	tmp = detector.detect_faces(srcimg)
	if len(tmp) == 0:
		print('no face')
		return None
	else:
		box = tmp[0]['box']
		tmp = tmp[0]['keypoints']
		landmark = []
		for t in list(tmp.items()):
			for tt in t[1]:
				landmark.append(tt)
	img = srcimg
	for i in range(5):
		cv2.circle(img, (landmark[i * 2], landmark[i * 2 + 1]), 1, (0, 255, 0), -1)
	cv2.rectangle(img, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]), (0, 255, 0), 1)
	cv2.imwrite('eval.png', img)
	with open('eval.png', "rb") as f:
		result = base64.b64encode(f.read())
	# os.remove('eval.png')
	return str(result, encoding="utf-8")

# MTCNN检测人脸测试
# if __name__ == '__main__':
# 	src = 'D:\python_project\my_blog\\test.png'
# 	with open(src, "rb") as f:
# 		base64_data = base64.b64encode(f.read())
# 	test1(base64_data)

# SphereFace识别人脸测试
# if __name__ == '__main__':
# 	# print(os.getcwd())
# 	# test()
# 	print(identfiy_all("me.jpg"))

# identfiy_all('me.jpg')