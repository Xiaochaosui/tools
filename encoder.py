# -*- coding: utf-8 -*-
# import cv2
import os
# import numpy as np
from Crypto.Cipher import AES


# root='/raid/zhangziyi/dataset/TL_aachen/'
# # ImagePath_2048 =root+'/image/'
# input_obj_xml =root+'Annotations/'
# # input_seg_xml =root+'/voc_seg_xml/'
#
# output_obj_txt =root+'/voc_obj/'
# # output_seg_txt =root+'/voc_seg/'
#
# if not os.path.exists(output_obj_txt):
#     os.makedirs(output_obj_txt)
# # if not os.path.exists(output_seg_txt):
# #     os.makedirs(output_seg_txt)
# xmllist = os.listdir(input_obj_xml)

def encode_txt(input_xml,output_txt,image):
    fs = open(input_xml, 'rb')
    fs_msg = fs.read()
    fs.close()
    key = b'heyun$8888$heyun'
    iv = b'\x9c\x05]^\xe5\xfb\xa7\x02\x94iT=\x8b\xf2\x0b\x8e'
    mycipher = AES.new(key, AES.MODE_CFB, iv)
    image_type=image.split('.')[-1]
    f_write_en = open(output_txt + image[:-(len(image_type)+1)] + '.txt', 'wb+')
    ciptext = iv + mycipher.encrypt(fs_msg)
    f_write_en.write(ciptext)
    f_write_en.close()

# for xml in xmllist:
#
#     image_type = 'jpg'
#     image = xml[:-(len(image_type)+1)] + '.jpg'
#     obj_xml_name=input_obj_xml+xml
#     # seg_xml_name = input_seg_xml + image[:-(len(image_type)+1)]  + '.xml'
#     # if os.path.exists(seg_xml_name):
#     #     encode_txt(seg_xml_name, output_seg_txt, image)
#
#     encode_txt(obj_xml_name,output_obj_txt,image)





