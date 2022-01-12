# -*- coding: utf-8 -*-

import os
# import numpy as np
from Crypto.Cipher import AES
import shutil
#


def decode_xml(input_text,output_xml,image):
    image_type = image.split('.')[-1] # jpg
    fs_obj = open(input_text, 'rb')
    ciptext1 = fs_obj.read()
    fs_obj.close()

    key = b'heyun$8888$heyun'
    mydecrypt = AES.new(key, AES.MODE_CFB, ciptext1[:16])
    decrytext = mydecrypt.decrypt(ciptext1[16:])

    f_write_de = open(output_xml + image[:-(len(image_type)+1)] + '.xml', 'w')
    f_write_de.write(decrytext.decode())
    f_write_de.close()

    with open(output_xml + image[:-(len(image_type)+1)] + '.xml', encoding='gb18030') as fobj:
        content = fobj.read()
    with open(output_xml + image[:-(len(image_type)+1)] + '.xml', 'w', encoding='utf-8') as fobj:
        fobj.write(content)



if __name__ == '__main__':

    root=  r'C:\Users\Public\Nwt\cache\recv\寇恒玮/'
    for i in range(1,5):
        # root_1 =  root +str(i)
        input_obj_txt =root+'/xml/'
        input_obj_img = root+'/image/'
        output_obj_xml =root + r'/res/xml/'
        output_obj_image = root + r'/res/image/'
        if not os.path.exists(output_obj_image):
            os.makedirs(output_obj_image)
        if not os.path.exists(output_obj_xml):
            os.makedirs(output_obj_xml)

        imglist = os.listdir(input_obj_img)
        for img in imglist:
            img_old = os.path.join(input_obj_img,img)
            img_new = os.path.join(output_obj_image,img)
            shutil.copy(img_old,img_new)


        txtlist = os.listdir(input_obj_txt)

        for txt in txtlist:
            image_type = 'jpg'
            # print (txt)
            image = txt[:-(len(image_type)+1)] + '.jpg'
            obj_txt_name=input_obj_txt+txt
            # seg_txt_name = input_seg_txt + image[:-(len(image_type)+1)] + '.txt'
            # if os.path.exists(seg_txt_name):
            #     decode_xml(seg_txt_name, output_seg_xml, image)
            decode_xml(obj_txt_name,output_obj_xml,image)
        


