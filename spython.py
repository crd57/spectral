# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:   spython
   Author:      crd
   date:        2018/4/22
-------------------------------------------------
"""
from spectral import *
from spectral.io import envi

img = open_image('92AV3C.lan')
img_band3 = img.read_band(2)  # 读取某个波段的信息
img_band3s = img.read_bands()  # 读取多个波段的信息
img_pixel = img.read_pixel(3, 5)  # 读取某个像素的光谱信息
img_subregion = img.read_subregion([25, 28], [35, 36])  # 读取某各子区域的光谱信息
img_subimg = img.read_subimage(25, 26, 27)  # 读取特定行，列，波段的光谱信息
arr = img.load()  # 转矩阵
img = envi.open('cup95eff.int.hdr', 'cup95eff.int')  # ENVI读取
view = imshow(img, (29, 19, 9))  # 展示影像
