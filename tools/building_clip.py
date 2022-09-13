import os
import cv2
import numpy as np

im1_path = 'D://code//mmsegmentation//New//img_dir//val'
im2_path = 'D://code//mmsegmentation//my_result//swin1//images'

num = len(os.listdir(im1_path))
for i in range(num):

    img1 = cv2.imread(os.path.join(im1_path, os.listdir(im1_path)[i]))
    img2 = cv2.imread(os.path.join(im2_path,os.listdir(im2_path)[i]), cv2.IMREAD_GRAYSCALE)
    h,w,c = img1.shape
    img3 = np.zeros((h,w,4))
    img3[:,:,0:3] = img1
    img3[:,:,3] = img2

    cv2.imwrite('D:\code\mmsegmentation\my_result\_final_result_swin\ ' + '%s.png' % os.listdir(im1_path)[i], img3)
