from cv2 import cv2
import numpy as np
import os
# 分割后的图片的文件夹，以及拼接后要保存的文件夹
pic_path = 'H:/FAANet/Pre/CHLandsat8/joint/'
pic_target = 'H:/FAANet/Pre/38_Cloud_Train/CHLandsat8-joint/'
# 数组保存分割后图片的列数和行数，注意分割后图片的格式为x_x.jpg，x从1开始
num_width_list = []
num_lenght_list = []
# 读取文件夹下所有图片的名称
picture_names = os.listdir(pic_path)
if len(picture_names)==0:
    print("没有文件")
else:
    # 获取分割后图片的尺寸
    img_1_1 = cv2.imread(pic_path + 'patch_1_1_by_1_LC08_L1TP_117040_20210625_20210630_01_T1.png')
    (width, length, depth) = img_1_1.shape
    # 分割名字获得行数和列数，通过数组保存分割后图片的列数和行数
    for picture_name in picture_names:
        num_width_list.append(int(picture_name.split("_")[-10]))
        num_lenght_list.append(int((picture_name.split("_")[-8])))
    # 取其中的最大值
    num_width = max(num_width_list)
    num_length = max(num_lenght_list)
    # 预生成拼接后的图片
    splicing_pic = np.zeros((num_width*width, num_length*length, depth))
    # 循环复制
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

