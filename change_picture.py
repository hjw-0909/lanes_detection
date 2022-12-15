# -*- coding:utf-8 -*-
import cv2 as cv
import os

for filename_1 in os.listdir('work_test_sim_shape'):
    for filename_2 in os.listdir('work_test_2'):
        if filename_1 == filename_2:
            img_1 = cv.imread('work_test_sim_shape' + '/' + filename_1)
            img_2 = cv.imread('work_test_2' + '/' + filename_2)
            img = cv.vconcat([img_1, img_2])
            img_name = "picture_loss/" + str(filename_1)
            cv.imwrite(img_name, img)
            break

path = 'picture_loss'
nums = len(os.listdir(path))
print(nums)




