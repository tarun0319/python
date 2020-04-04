

import cv2
import numpy as np
import  imutils


img_org = cv2.imread('car6.jpg')
size = np.shape(img_org)
if size[0] <= 776:
    img_org = imutils.resize(img_org , 900)

img_org2 = img_org.copy()
img_bw = cv2.cvtColor(img_org , cv2.COLOR_BGR2GRAY)


ret3,img_thr = cv2.threshold(img_bw,125,255,cv2.THRESH_BINARY)


cv2.imwrite('thresh.jpg',img_thr)

img_edg  = cv2.Canny(img_thr ,100,200)

cv2.imwrite('cn_edge.jpg' , img_edg)



kernel = cv2.getStructuringElement(cv2.MORPH_DILATE, (7, 7))
img_dil = cv2.dilate(img_edg, kernel, iterations = 1)

cv2.imwrite('dilated_img.jpg',img_dil)


#if  you  are  using  opencv 2.X then  make  sure  to  remove  "something_else " variable  from  list  below

(contours ,hierarchye) = cv2.findContours(img_dil.copy(), 1, 2)
cnts = sorted(contours, key = cv2.contourArea, reverse = True)[:10]

screenCnt = None

for c in cnts:
	# approximate the contour
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)

	# if our approximated contour has four points, then
	# we can assume that we have found our screen
	if len(approx) == 4:
		screenCnt = approx
		break





mask = np.zeros(img_bw.shape, dtype=np.uint8)
roi_corners = np.array(screenCnt ,dtype=np.int32)
ignore_mask_color = (255,)*1
cv2.fillPoly(mask, roi_corners , ignore_mask_color)
cv2.drawContours(img_org, [screenCnt], -40, (100, 255, 100), 9)
cv2.imshow('original  image with boundry' , img_org)
cv2.imwrite('plate_detedted.jpg',img_org)


ys =[screenCnt[0,0,1] , screenCnt[1,0,1] ,screenCnt[2,0,1] ,screenCnt[3,0,1]]
xs =[screenCnt[0,0,0] , screenCnt[1,0,0] ,screenCnt[2,0,0] ,screenCnt[3,0,0]]

ys_sorted_index = np.argsort(ys)
xs_sorted_index = np.argsort(xs)

x1 = screenCnt[xs_sorted_index[0],0,0]
x2 = screenCnt[xs_sorted_index[3],0,0]

y1 = screenCnt[ys_sorted_index[0],0,1]
y2 = screenCnt[ys_sorted_index[3],0,1]



img_plate = img_org2[y1:y2 , x1:x2]


# for i in screenCnt:
#     print(i)
#
# print xs , ys
#
# print x1,x2,y1,y2





cv2.imshow('number plate',img_plate)

cv2.imwrite('number_plate.jpg',img_plate)
cv2.waitKey(0)