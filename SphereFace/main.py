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


def tell(imglist, thd=0.3085):
	img = np.vstack(imglist)
	img = Variable(torch.from_numpy(img).float(), volatile=True)
	output = net(img)
	f = output.data
	f1, f2 = f[0], f[2]
	cosdistance = f1.dot(f2) / (f1.norm() * f2.norm() + 1e-5)
	if (cosdistance > thd):
		return True
	else:
		return False


def test(srcimg='./face/me.jpg'):
	##############img1###################
	srcimg = srcimg
	landmark, _ = generate_landmark(srcimg)
	img1 = alignment(cv2.imread(srcimg), landmark)
	##############img2###################
	cap = cv2.VideoCapture(0)
	while (1):
		# get a frame
		ret, frame = cap.read()
		# show a frame
		cv2.imwrite('tmp.png', frame)
		landmark, box = generate_landmark('tmp.png')
		if len(landmark) == 0:
			cv2.imshow("capture", frame)
			continue
		for i in range(5):
			cv2.circle(frame, (landmark[i * 2], landmark[i * 2 + 1]), 1, (0, 255, 0), -1)
		cv2.rectangle(frame, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]), (0, 255, 0), 1)
		cv2.imshow("capture", frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			cv2.imwrite("eval.png", frame)
			break
	cap.release()
	cv2.destroyAllWindows()
	evalimg = 'eval.png'
	landmark, _ = generate_landmark(evalimg)
	img2 = alignment(cv2.imread(evalimg), landmark)
	#####################################
	imglist1 = [img1, cv2.flip(img1, 1), img2, cv2.flip(img2, 1)]
	for i in range(len(imglist1)):
		imglist1[i] = imglist1[i].transpose(2, 0, 1).reshape((1, 3, 112, 96))
		imglist1[i] = (imglist1[i] - 127.5) / 128.0

	if (tell(imglist1)):
		print('浩聪')
	else:
		print('不是浩聪')


if __name__ == '__main__':
	test()
