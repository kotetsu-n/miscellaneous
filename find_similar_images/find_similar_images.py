import argparse
import cv2
import math
import numpy as np
import os
import glob
import shutil
def compare_2images(img1, img2):
	akaze = cv2.AKAZE_create()                                

	kp1, des1 = akaze.detectAndCompute(img1, None)
	kp2, des2 = akaze.detectAndCompute(img2, None)

	bf = cv2.BFMatcher()
	matches = bf.knnMatch(des1, des2, k=2)

	ratio = 0.7
	good = []
	for m, n in matches:
		if m.distance < ratio * n.distance:
			good.append([m])
	# good = matches

	return good, kp1, kp2, 
	
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("-sdir", "--src_dir", type=str, default='./src', help="Path to src image")
	parser.add_argument("-cdir", "--compare_dir", default='./compare', \
						type=str, help="path to compare images")
	parser.add_argument('-rdir', '--remove_dir', default='./removed')
	parser.add_argument("-min", "--min_features", default=30, \
						type=int, help="threshold of the similarity")
	args = parser.parse_args()

	os.makedirs(args.remove_dir, exist_ok=True)
	src_image_paths = glob.glob(os.path.join(args.src_dir, '*'))
	compare_image_paths = glob.glob(os.path.join(args.compare_dir, '*'))

	akaze = cv2.AKAZE_create()                                

	resize_ratio1 = 1.0
	resize_ratio2 = 1.0
	base_size = 1024

	for src_path in src_image_paths:
		print(src_path)
		if os.path.exists(src_path):
			src = cv2.imread(src_path)
		else:
			continue

		h, w, _ = src.shape
		resize_ratio1 = base_size / h if h > w else base_size / w

		s_src = cv2.resize(src,(int(w*resize_ratio1), int(h*resize_ratio1)))
		img1 = cv2.cvtColor(s_src, cv2.COLOR_BGR2GRAY)
		kp1, des1 = akaze.detectAndCompute(img1, None)

		for com_path in compare_image_paths:
			print(com_path)
			if os.path.exists(com_path):
				con = cv2.imread(com_path)
			else:
				continue
			print(src.shape, con.shape)

			h, w, _ = con.shape
			resize_ratio2 = base_size / h  if h > w else base_size / w
			
			s_con = cv2.resize(con,(int(w*resize_ratio2), int(h*resize_ratio2)))
			img2 = cv2.cvtColor(s_con, cv2.COLOR_BGR2GRAY)

			kp2, des2 = akaze.detectAndCompute(img2, None)

			bf = cv2.BFMatcher()
			matches = bf.knnMatch(des1, des2, k=2)

			ratio = 0.7
			good = []
			for m, n in matches:
				if m.distance < ratio * n.distance:
					good.append([m])

			# good, kp1, kp2 = compare_2images(img1, img2)
			print(len(good))
			if len(good) > args.min_features:
				matched_img = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)
				cv2.imshow('preview', matched_img)
				key = cv2.waitKey(0)
				if key == ord('r'):
					shutil.move(com_path, args.remove_dir)
				elif key == ord('l'):
					shutil.move(src_path, args.remove_dir)
				# cv2.destroyAllWindows()
				cv2.destroyWindow('preview')