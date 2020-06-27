import argparse
import cv2
import math
import numpy as np
import os
import glob

vertice = []
img = None
max_resol = 1024
output_dir = './cropped'
img_name = None

preview_pos = None
cropped_pos = None

def organize_point_order(verts):
	tx, ty = 0, 0
	for i in range(4):
		tx += verts[i][0]
		ty += verts[i][1]
	avg_x = tx*0.25
	avg_y = ty*0.25
	 
	organized_pts = []
	for i in range(4):
		if verts[i][0] < avg_x and verts[i][1] < avg_x:
			organized_pts.append([verts[i][0], verts[i][1]])
		if verts[i][0] > avg_x and verts[i][1] < avg_x:
			organized_pts.append([verts[i][0], verts[i][1]])
		if verts[i][0] > avg_x and verts[i][1] > avg_x:
			organized_pts.append([verts[i][0], verts[i][1]])
		if verts[i][0] < avg_x and verts[i][1] > avg_x:
			organized_pts.append([verts[i][0], verts[i][1]])
	return organized_pts

def mouse_event(event, x, y, flags, param):
	global img, vertice, preview_pos, cropped_pos
	if event == cv2.EVENT_LBUTTONDOWN:
		pass
		# print(x, y)
		# refPt = [(x, y)]
	elif event == cv2.EVENT_LBUTTONUP:
		vertice.append((x, y))

		if len(vertice) == 5:
			min_dist = 100000
			replace_id = -1
			for i in range(4):
				t_dist = math.sqrt((vertice[-1][0]-vertice[i][0])**2 + (vertice[-1][1]-vertice[i][1])**2)
				if t_dist < min_dist:
					min_dist = t_dist
					replace_id = i
			vertice[replace_id] = vertice[-1]
			vertice.pop()

		if len(vertice) == 4:
			vertice = organize_point_order(vertice)
			h_l1 = math.sqrt((vertice[0][0]-vertice[1][0])**2+((vertice[0][1]-vertice[1][1])**2))
			h_l2 = math.sqrt((vertice[2][0]-vertice[3][0])**2+((vertice[2][1]-vertice[3][1])**2))
			v_l1 = math.sqrt((vertice[1][0]-vertice[2][0])**2+((vertice[1][1]-vertice[2][1])**2))
			v_l2 = math.sqrt((vertice[3][0]-vertice[0][0])**2+((vertice[3][1]-vertice[0][1])**2))
			aspect_ratio = 0.5 * (h_l1 / v_l1 + h_l2 / v_l2)
			if aspect_ratio >= 1.0: #horizontal
				w = max_resol
				h = max_resol * (1.0 / aspect_ratio)
			else:
				w = max_resol * aspect_ratio
				h = max_resol
			src_vertice = np.asarray(vertice, dtype=np.float32)
			dst_vertice = np.array([[0,0], [w,0], [w,h], [0,h]], dtype=np.float32)
			M = cv2.getPerspectiveTransform(src_vertice, dst_vertice)
			dst = cv2.warpPerspective(img, M, (int(w), int(h)), flags=cv2.INTER_AREA)

			pts = np.asarray(vertice, dtype=np.int32)
			pts = pts.reshape((-1, 1, 2)) 
			img_for_draw = img.copy()
			cv2.polylines(img_for_draw, [pts], True, (0, 0, 255), 2)
			cv2.imshow("image", img_for_draw)

			key = cv2.waitKey(1)
			cv2.imshow('frontalized', dst)
			cv2.moveWindow('frontalized', *cropped_pos)
			key = cv2.waitKey(0)
			if key == ord('s'):
				cv2.imwrite(os.path.join(output_dir, img_name), dst)
				print(output_dir, img_name)
				vertice = []
				# go_to_next = True
			elif key == ord('y'):
				pass
			cv2.destroyWindow('frontalized')
			# cv2.imshow("image", img)
		
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	# parser.add_argument("-i", "--image", default='test.jpg', 
	# 					required=True, help="Path to the image")
	parser.add_argument("-d", "--image_dir", default='./src_images', 
						required=True, help="Path to the image")
	parser.add_argument("-r", "--resol", default=1024, type=int,
						help="maximum resolution")
	parser.add_argument("-o", "--output_dir", default='./cropped', 
						help="Path to output image")
	parser.add_argument("-dx1", "--display_pos_x1", default=2000,
						type=int, help="preview window position")
	parser.add_argument("-dy1", "--display_pos_y1", default=0,
						type=int, help="preview window position")
	parser.add_argument("-dx2", "--display_pos_x2", default=2200,
						type=int, help="preview cropped window position")
	parser.add_argument("-dy2", "--display_pos_y2", default=0,
						type=int, help="preview cropped window position")
	args = parser.parse_args()

	max_resol = args.resol
	output_dir = args.output_dir
	os.makedirs(output_dir, exist_ok=True)

	preview_pos = [args.display_pos_x1, args.display_pos_y1]
	cropped_pos = [args.display_pos_x2, args.display_pos_y2]

	img_paths = glob.glob(os.path.join(args.image_dir, '*.jpg'))
	pngs = glob.glob(os.path.join(args.image_dir, '*.png'))
	img_paths.extend(pngs)
	
	for img_path in img_paths:
		img_name = os.path.basename(img_path)
		img = cv2.imread(img_path)

		test = cv2.namedWindow('image')
		cv2.moveWindow('image', *preview_pos)
		cv2.setMouseCallback('image', mouse_event)

		while (True):
			cv2.imshow("image", img)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				vertice = []
				break