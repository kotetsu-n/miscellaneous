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
	src_image_paths.sort()
	compare_image_paths.sort()

	isSameFolder = True if args.src_dir == args.compare_dir else False
	print(args.src_dir)
	print(args.compare_dir)
	print(f'isSameFolder:{isSameFolder}')

	akaze = cv2.AKAZE_create()                                

	# resize_ratio1 = 1.0
	# resize_ratio2 = 1.0
	base_size = 512
 
	src_feature_dict = {}
	com_feature_dict = {}

	for i, src_path in enumerate(src_image_paths):
		print(i, src_path)
		if os.path.exists(src_path):
			src = cv2.imread(src_path)
			# print(src.shape)
		else:
			print('not exist')
			continue

		h, w, _ = src.shape
		resize_ratio = base_size / h if h > w else base_size / w

		s_src = cv2.resize(src,(int(w*resize_ratio), int(h*resize_ratio)))
		img = cv2.cvtColor(s_src, cv2.COLOR_BGR2GRAY)
		kp, des = akaze.detectAndCompute(img, None)

		src_feature_dict[i] = {'path':src_path, 'kp':kp, 'des':des, 'ratio':resize_ratio, 'exist':True}
		print(len(kp))
	
	# print(src_feature_dict)

	if not isSameFolder:
		for i, src_path in enumerate(compare_image_paths):
			print(i, src_path)
			if os.path.exists(src_path):
				src = cv2.imread(src_path)
			else:
				continue

			h, w, _ = src.shape
			resize_ratio = base_size / h if h > w else base_size / w

			s_src = cv2.resize(src,(int(w*resize_ratio), int(h*resize_ratio)))
			img = cv2.cvtColor(s_src, cv2.COLOR_BGR2GRAY)
			kp, des = akaze.detectAndCompute(img, None)

			com_feature_dict[i] = {'path':src_path, 'kp':kp, 'des':des, 'ratio':resize_ratio, 'exist':True}
	else:
		com_feature_dict = src_feature_dict.copy()

	bf = cv2.BFMatcher()

	
	for i, (sk, sv) in enumerate(src_feature_dict.items()):
		for j, (ck, cv) in enumerate(com_feature_dict.items()):
			if isSameFolder and i >= j:
				continue
			sp, sk, sd, sr, se = sv['path'], sv['kp'], sv['des'], sv['ratio'], sv['exist']
			cp, ck, cd, cr, ce = cv['path'], cv['kp'], cv['des'], cv['ratio'], cv['exist']
			# print(i, j, len(sk), len(ck))
			if len(sk) == 0 or len(ck) == 0:
				continue
			if se is False or ce is False:
				continue
			
			matches = bf.knnMatch(sd, cd, k=2)
				
			ratio = 0.7
			good = []
			for m, n in matches:
				if m.distance < ratio * n.distance:
					good.append([m])

			if len(good) > args.min_features:
				img1 = cv2.imread(sp)
				img2 = cv2.imread(cp)
				h1, w1, _ = img1.shape
				h2, w2, _ = img2.shape
				print(f'({w1}, {h1}), ({w2}, {h2})')
				img1 = cv2.resize(img1, (int(w1*sr), int(h1*sr)))
				img2 = cv2.resize(img2, (int(w2*cr), int(h2*cr)))
				matched_img = cv2.drawMatchesKnn(img1, sk, img2, ck, good, None, flags=2)
				cv2.imshow('preview', matched_img)
				key = cv2.waitKey(0)
				if key == ord('r'):
					shutil.move(cp, args.remove_dir)
					com_feature_dict[j]['exist'] = False
					if isSameFolder:
						src_feature_dict[j]['exist'] = False
					# del com_feature_dict[j]
				elif key == ord('l'):
					shutil.move(sp, args.remove_dir)
					src_feature_dict[i]['exist'] = False
					if isSameFolder:
						com_feature_dict[i]['exist'] = False
						# del com_feature_dict[i]
					cv2.destroyWindow('preview')
					break
				cv2.destroyWindow('preview')
				# cv2.destroyAllWindows()
		# if isSameFolder:
		# 	src_feature_dict = com_feature_dict.copy()