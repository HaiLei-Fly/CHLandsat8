from cv2 import cv2
import numpy as np
import os

pic_path = 'H:/FAANet/Pre/CHLandsat8/joint/'
pic_target = 'H:/FAANet/Pre/38_Cloud_Train/CHLandsat8-joint/'

num_width_list = []
num_lenght_list = []

picture_names = os.listdir(pic_path)
if len(picture_names)==0:
    print("none")
else:

    img_1_1 = cv2.imread(pic_path + 'patch_1_1_by_1_LC08_L1TP_117040_20210625_20210630_01_T1.png')
    (width, length, depth) = img_1_1.shape

    for picture_name in picture_names:
        num_width_list.append(int(picture_name.split("_")[-10]))
        num_lenght_list.append(int((picture_name.split("_")[-8])))

    num_width = max(num_width_list)
    num_length = max(num_lenght_list)

    splicing_pic = np.zeros((num_width*width, num_length*length, depth))

    for idx in range(0, 1):
        k = 0
        splicing_pic = np.zeros((num_width*width, num_length*length, depth))
        for i in range(1, num_width+1):
            for j in range(1, num_length+1):
                    k += 1
                    img_part = cv2.imread(pic_path + 'patch_{}_{}_by_{}_LC08_L1TP_117040_20210625_20210630_01_T1.png'.format(k, i, j),1)         
                    splicing_pic[ width*(i-1) : width*i, length*(j-1) : length*j, :] = img_part
                    print(splicing_pic.shape)
        cv2.imwrite(pic_target + 'LC08_L1TP_' + picture_names[idx].split("_")[-5] + '_' +  picture_names[idx].split("_")[-4] + '_'  +  picture_names[idx].split("_")[-3]  + '_01_T1.png', splicing_pic)
    print("done!!!")

