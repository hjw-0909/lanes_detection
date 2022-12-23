# -*- coding:utf-8 -*-
import cv2 as cv
import os
i = 1
for filename_1 in os.listdir('work_test_sim_r1'):
    for filename_2 in os.listdir('work_test_2'):
        if filename_1 == filename_2:
            img_1 = cv.imread('work_test_sim_r1' + '/' + filename_1)
            img_2 = cv.imread('work_test_2' + '/' + filename_2)
            img = cv.vconcat([img_1, img_2])
            img_name = "picture_com/" + str(filename_1)
            cv.imwrite(img_name, img)
            print(str(i) + ' images have been processed!')
            i += 1
            break

path = 'picture_com'
nums = len(os.listdir(path))
print(nums)