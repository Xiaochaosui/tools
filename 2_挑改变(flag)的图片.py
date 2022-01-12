# @Author:xiaochaosui
# @Organization:FiberHome
# @Email:chaosuixiao@gmail.com
# @Time:2021/11/18 15:00
import os
import xml.etree.ElementTree as ET
import re
import shutil
from  decoder import decode_xml

def copyImg(source,dest):
    temple = source.replace(".xml",".jpg")

    img_path = temple.replace("xml",'image')

    shutil.copy(img_path,dest)

def readXml(file,new_img_path,new_xml_path):
    global n
    # print("="*5,file,"="*5)
    try:
        tree = ET.parse(file)
        root = tree.getroot()
        for object in root.findall("object"):
            if object.findall("name")[0].text =="flag":
                n+=1
                copyImg(file,new_img_path)
                shutil.copy(file,new_xml_path)
                print(file)

    except:
        print("error_xml.txt",file.split('xml\\')[-1]+'\n')
        # print(file.split('xml\\'))
        with open("error_xml.txt",'a')  as f:
            f.write(file.split('xml\\')[1]+'\n')


if __name__ == '__main__':

    # 最后的结果在 root路径下的 result下的final
    root =r"D:\xcsy\245_246\挑数据\2\Tl\\" # 推理完的图片的根目录
    root_path = root + r"result"  # output的路径



    for i in range(1, 5):
        root_1 = root + str(i)
        input_obj_txt = root_1 + '/output/voc_obj/'
        input_obj_img = root_1 + '/img/'
        output_obj_xml = root + r'/result/xml/'
        output_obj_image = root + r'/result/image/'
        if not os.path.exists(output_obj_image):
            os.makedirs(output_obj_image)
        if not os.path.exists(output_obj_xml):
            os.makedirs(output_obj_xml)

        imglist = os.listdir(input_obj_img)
        for img in imglist:
            img_old = os.path.join(input_obj_img, img)
            img_new = os.path.join(output_obj_image, img)
            shutil.copy(img_old, img_new)

        txtlist = os.listdir(input_obj_txt)

        for txt in txtlist:
            image_type = 'jpg'
            # print (txt)
            image = txt[:-(len(image_type) + 1)] + '.jpg'
            obj_txt_name = input_obj_txt + txt
            # seg_txt_name = input_seg_txt + image[:-(len(image_type)+1)] + '.txt'
            # if os.path.exists(seg_txt_name):
            #     decode_xml(seg_txt_name, output_seg_xml, image)
            decode_xml(obj_txt_name, output_obj_xml, image)


    xml_path = root_path + r"\xml"  # 原始xml路径
    img_path = root_path + r"\image"  # 原始img路径
    dest_path = root_path + r"\final"
    new_xml_path = dest_path + r"\xml\\"  # 把改变的xml复制到结果文件夹路径
    new_img_path = dest_path + r"\image\\" # 把改变的图片复制到结果文件夹路径
    n = 0
    if not os.path.isdir(new_xml_path):
        os.makedirs(new_xml_path)
    if not os.path.isdir(new_img_path):
        os.makedirs(new_img_path)


    xmlsName = os.listdir(xml_path)
    print("所有图片数量:",len(xmlsName))
    for xmlName in xmlsName:
        xmlFile = os.path.join(xml_path, xmlName)
        # print(xmlFile)
        readXml(xmlFile,new_img_path,new_xml_path)
    print("需要新加的img数量:",n)
