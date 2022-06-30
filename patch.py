# -*- coding:utf-8 -*-
import os
import matplotlib.pyplot as plt
import cv2
import numpy as np
import math
import glob


def crop_one_picture(path,filename,cols,rows):
    img=cv2.imread(path+filename,1)#
    # img=cv2.imread(path+filename,-1) # mask
    # img= cv2.copyMakeBorder(img, top=97, bottom=98, left=152, right=153,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 1
    # img= cv2.copyMakeBorder(img, top=87, bottom=88, left=147, right=148,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 2
    # img= cv2.copyMakeBorder(img, top=137, bottom=138, left=36, right=37,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 3
    # img= cv2.copyMakeBorder(img, top=132, bottom=133, left=31, right=32,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 4
    # img= cv2.copyMakeBorder(img, top=12, bottom=13, left=62, right=63,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 5
    # img= cv2.copyMakeBorder(img, top=107, bottom=108, left=6, right=7,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 6
    # img= cv2.copyMakeBorder(img, top=107, bottom=108, left=167, right=168,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 7
    # img= cv2.copyMakeBorder(img, top=97, bottom=98, left=162, right=163,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 8
    # img= cv2.copyMakeBorder(img, top=82, bottom=83, left=152, right=153,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 9
    # img= cv2.copyMakeBorder(img, top=57, bottom=58, left=122, right=123,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 10
    # img= cv2.copyMakeBorder(img, top=6, bottom=7, left=81, right=82,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 11
    # img= cv2.copyMakeBorder(img, top=62, bottom=63, left=112, right=113,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 12
    # img= cv2.copyMakeBorder(img, top=22, bottom=23, left=67, right=68,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 13
    # img= cv2.copyMakeBorder(img, top=127, bottom=128, left=16, right=17,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 14
    # img= cv2.copyMakeBorder(img, top=21, bottom=22, left=101, right=102,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 15
    # img= cv2.copyMakeBorder(img, top=158, bottom=159, left=27, right=28,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 16
    # img= cv2.copyMakeBorder(img, top=31, bottom=32, left=106, right=107,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 17
    # img= cv2.copyMakeBorder(img, top=97, bottom=98, left=152, right=153,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 18
    # img= cv2.copyMakeBorder(img, top=152, bottom=153, left=51, right=52,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 19
    # img= cv2.copyMakeBorder(img, top=142, bottom=143, left=51, right=52,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 20
    img= cv2.copyMakeBorder(img, top=167, bottom=168, left=61, right=62,
                        borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 21
    # img= cv2.copyMakeBorder(img, top=132, bottom=133, left=31, right=32,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 22
    # img= cv2.copyMakeBorder(img, top=152, bottom=153, left=41, right=42,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 23
    # img= cv2.copyMakeBorder(img, top=82, bottom=83, left=147, right=148,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 24
    # img= cv2.copyMakeBorder(img, top=16, bottom=17, left=91, right=92,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 25
    # img= cv2.copyMakeBorder(img, top=57, bottom=58, left=122, right=123,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 26
    # img= cv2.copyMakeBorder(img, top=82, bottom=83, left=147, right=148,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 27
    # img= cv2.copyMakeBorder(img, top=52, bottom=53, left=117, right=118,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 28
    # img= cv2.copyMakeBorder(img, top=137, bottom=138, left=36, right=37,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 29
    # img= cv2.copyMakeBorder(img, top=132, bottom=133, left=26, right=27,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 30
    # img= cv2.copyMakeBorder(img, top=47, bottom=48, left=102, right=103,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 31
    # img= cv2.copyMakeBorder(img, top=172, bottom=173, left=66, right=67,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 32
    # img= cv2.copyMakeBorder(img, top=1, bottom=2, left=61, right=62,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 33
    # img= cv2.copyMakeBorder(img, top=16, bottom=17, left=91, right=92,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 34
    # img= cv2.copyMakeBorder(img, top=152, bottom=153, left=51, right=52,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 35
    # img= cv2.copyMakeBorder(img, top=107, bottom=108, left=172, right=173,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 36
    # img= cv2.copyMakeBorder(img, top=112, bottom=113, left=167, right=168,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 37
    # img= cv2.copyMakeBorder(img, top=92, bottom=93, left=147, right=148,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 38
    # img= cv2.copyMakeBorder(img, top=87, bottom=88, left=147, right=148,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 39
    # img= cv2.copyMakeBorder(img, top=12, bottom=13, left=72, right=73,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 40
    # img= cv2.copyMakeBorder(img, top=127, bottom=128, left=11, right=12,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 41
    # img= cv2.copyMakeBorder(img, top=112, bottom=113, left=1, right=2,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 42
    # img= cv2.copyMakeBorder(img, top=11, bottom=12, left=76, right=77,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 43
    # img= cv2.copyMakeBorder(img, top=157, bottom=158, left=51, right=52,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 44
    ####### Test
    # img= cv2.copyMakeBorder(img, top=142, bottom=143, left=46, right=47,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 1
    # img= cv2.copyMakeBorder(img, top=67, bottom=68, left=127, right=128,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 2
    # img= cv2.copyMakeBorder(img, top=132, bottom=133, left=36, right=37,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 3
    # img= cv2.copyMakeBorder(img, top=127, bottom=128, left=16, right=17,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 4
    # img= cv2.copyMakeBorder(img, top=21, bottom=22, left=106, right=107,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 5
    # img= cv2.copyMakeBorder(img, top=127, bottom=128, left=11, right=12,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 6
    # img= cv2.copyMakeBorder(img, top=102, bottom=103, left=167, right=168,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 7
    # img= cv2.copyMakeBorder(img, top=97, bottom=98, left=162, right=163,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 8
    # img= cv2.copyMakeBorder(img, top=132, bottom=133, left=16, right=17,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 9
    # img= cv2.copyMakeBorder(img, top=107, bottom=108, left=1, right=2,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 10
    # img= cv2.copyMakeBorder(img, top=31, bottom=32, left=111, right=112,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 11
    # img= cv2.copyMakeBorder(img, top=107, bottom=108, left=1, right=2,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 12
    # img= cv2.copyMakeBorder(img, top=21, bottom=22, left=96, right=97,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 13
    # img= cv2.copyMakeBorder(img, top=6, bottom=7, left=76, right=77,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 14
    # img= cv2.copyMakeBorder(img, top=152, bottom=153, left=46, right=47,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 15
    # img= cv2.copyMakeBorder(img, top=92, bottom=93, left=152, right=153,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 16
    # img= cv2.copyMakeBorder(img, top=6, bottom=7, left=81, right=82,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 17
    # img= cv2.copyMakeBorder(img, top=162, bottom=163, left=51, right=52,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 18
    # img= cv2.copyMakeBorder(img, top=162, bottom=163, left=61, right=62,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 19
    # img= cv2.copyMakeBorder(img, top=1, bottom=2, left=66, right=67,
    #                     borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0]) # 20
    
    sum_rows=img.shape[0]   
    sum_cols=img.shape[1]   
    save_path=path+"\\crop{0}_{1}\\".format(cols,rows) 
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    print("裁剪所得{0}列图片，{1}行图片.".format(int(sum_cols/cols),int(sum_rows/rows))) 
    k = 0
    for i in range(int(sum_rows/rows)):
        for j in range(int(sum_cols/cols)):
            k += 1
            # cv2.imwrite(save_path+'patch_{}_{}_by_{}_'.format(k, i+1, j+1)+ filename.split('.')[0] + os.path.splitext(filename)[1],img[i*cols:(i+1)*cols,j*rows:(j+1)*rows,:]) # L image
            cv2.imwrite(save_path+'patch_{}_{}_by_{}_'.format(k, i+1, j+1)+ filename.split('.')[0] + os.path.splitext(filename)[1],img[i*cols:(i+1)*cols,j*rows:(j+1)*rows]) # mask
    print("裁剪完成，得到{0}张图片.".format(int(sum_cols/cols)*int(sum_rows/rows)))
    print("文件保存在{0}".format(save_path))
    
if __name__ == '__main__':

    path='G:\\CHLandsat8\\LandsatNC\\Train\\patch\\'   
    picture_names = sorted(glob.glob(path  + '*.png'))
    num = 0
    for picture_name in picture_names:
        print(picture_name)
        name = picture_name.split('\\')[5] 
        print(name)
        crop_one_picture(path,name,352,352)
