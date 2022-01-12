# # @Author:xiaochaosui
# # @Organization:FiberHome
# # @Email:chaosuixiao@gmail.com
# # @Time:2021/9/28 14:14
# # tl_dict = { "tl_green":'0',
# #             "tl_red":'1',
# #             "tl_yellow":'2',
# #             "tl_none":'3'}
# # from pathlib import Path
# # print('tl_red'in tl_dict.keys())
# # file = "'run's/train/exp5/weights/best.pt"
# # file = Path(str(file).strip().replace("'", '').lower())
# # print(file.exists())
#
# import os
# file_path = os.getcwd() # 这是你的本文件的的目录
# project_path = os.path.split(file_path)
#
# # # root_path = os.path.dirname(project_path)
# # # print(root_path)
# # save_path = os.path.join(project_path,'pdks\\si_fab\\gdsii') # 这是你的.gds 要保存的文件夹
# # gds_nams = 'name.gds' # 这是你的gds名字
# # result = os.path.join(save_path,gds_nams) # 这就是你要最后写到保存那句话的路径
# # print(result)
# # from test.write import write
#
# def writeText(file,data):
#     with open(file,'a') as f:
#         f.write(data)
#
# # write('xcs.txt',"csd\n")
#
#
# # import shutil
# # shutil.copy('xcs.txt','test')
#
# import xml.etree.ElementTree as ET
# file = r'D:\xcsy\dataset\tl_green\c121f402-2e25ddb9.xml'
# try:
#     tree = ET.parse(file)
#     print("xcsss")
# except:
#     writeText("error_xml.txt", file.split('t\\')[1]+'\n')
#
# # data ="xcsy"
# # write(data)

import os
# print(f'\033[1;30;41m{"./runss/detect"}\033[0m')
# import math
# print(math.ceil(12/5))
# import random
# random.seed(10)
# colors = [[random.randint(0, 255) for _ in range(3)] for _ in range(20)]
# color = colors or [random.randint(0, 255) for _ in range(3)]
# a = 0
# b =2
# c = a or b
# print(c)
import torch
# device_nums = 8
# device = [str(x) for x in range(device_nums)]
# print(device)

# import time
# t1 = time.time()
# time.sleep(5)
# print(time.time()-t1)
# print(12.0//2)

# a = [1,2,3]
# a.clear()
# a.extend(b)
# print(a)

# xml_path = r'D:\xcsy\245\detect\res_test\All_Results\All_Annotations'
# img_path = r'D:\xcsy\245\detect\res_test\All_Results\JPEGImages'
# xml_names = os.listdir(xml_path)
# img_names = os.listdir(img_path)
#
# img_formate = img_names[0].split(".")[-1]
# print(img_formate)
# path = r'D:\xcsy\245_246\asd\asdas\qwew'
# os.makedirs(path)
# val = input("(Y) Continue,(N) Break:")
# print(val)
# while True:
#     print("aa")

path = r"D:\xcsy\245\detect"
inst = r"xcsy"


s1 = "x"
s2 =  "x"

# a= path + "/" + inst
# print(a)
# import numpy
# a = numpy.array([1,2,3])
#
# print(a**2)
d = {1:"a",2:"b"}

# a = list(d.keys())
# print(type(a))
# print(a)
# for x in d:

# import cv2
# def get_img_shape(img_file):
#     img = cv2.imread(img_file)
#     return img.shape[0],img.shape[1]
#
# if __name__ == '__main__':
#     h,w = get_img_shape(r"D:\xcsy\dataset\1\1611629017.938.jpg")  # 第一个是 h 第二个是 w
#     print(w,"x",h)

# w = 1280
# h = 720
# xmin = float(748.875)
# xmax = float(752.625)
# ymin = float(343.375)
# ymax = float(354.25)
# xcenter = (xmin + xmax) /2 / w
# ycenter = (ymin + ymax) / 2 / h
# rect_w = (xmax - xmin) / w
# rect_h = (ymax -ymin) / h
# print(xcenter,ycenter,rect_w,rect_h)

from pathlib import Path
import cv2
file = r"file:///D:/xcsy/dataset/plot_test/images/BF_0001114_58262_5.01_109.5680.jpg"

img = cv2.imread(file)
cv2.imshow("a",img)
cv2.waitKey()

# p  = Path(file)
#
# from tools import xml_get_object
# xml = r"D:/xcsy/dataset/plot_test/Annotation/2b590735-a3bf6ea0.xml"
# tree,root,objects = xml_get_object(xml)
# for obj in objects:
#     cls = obj.findall("name")[0].text.capitalize()
#     ID = obj.findall("ID")
#     print(ID)
#     if ID:
#         print("aaa")
#     else:
#         print("aaaaad")
