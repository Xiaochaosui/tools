# @Author:xiaochaosui
# @Organization:FiberHome
# @Email:chaosuixiao@gmail.com
# @Time:2021/9/27 10:24
from pathlib import Path
import os
import xml.etree.ElementTree as ET
import re
import shutil
from tools import mkdir
# tl_dict = { "tl_green":'0',
#             "tl_red":'1',
#             "tl_yellow":'2',
#             "tl_none":'3'}

# car_dict = {
    # "car":'0'
# }
# labels_dict = {"face":'0'}

# labels_dict = { "tl_green":'0',
#             "tl_red":'1',
#             "tl_yellow":'2'}
labels_list = ['vehicle', 'person', 'bike', 'motor', 'rider', 't_sign','tl_red', 'tl_green', 'tl_yellow', 'crosswalk','PM0100_导向箭头_直行','PM0300_导向箭头_左转','PM0400_导向箭头_右转','PM0500_导向箭头_直行或右转','PM0200_导向箭头_直行或左转','PM0600_导向箭头_掉头']

global labels_nums
# global g_nums
# global y_nums
# global r_nums
# global n_nums
# global car_nums
labels_nums = 0
# g_nums = 0
# y_nums = 0
# r_nums = 0
# n_nums = 0
# global r, y, n, g
# r, y, n, g = 0,0,0,0
def readXml(file):
    print("="*5,file,"="*5)
    try:
        tree = ET.parse(file)
        root = tree.getroot()
        w = int(root.findall("size")[0].findall("width")[0].text)
        h = int(root.findall("size")[0].findall("height")[0].text)
        # print(w,h)
        res = ''
        global labels_nums
        # global g_nums
        # global y_nums
        # global r_nums
        # global n_nums
        # print("$$$",len(root.findall("object")))
        for object in root.findall("object"):
            # print(object.findall("name")[0].text)
            # if object.findall("name")[0].text == "car": #tag 标签名 text 标签值
            cls = object.findall("name")[0].text
            # print(cls)
            # global r, y, n, g
            if cls in ['car','bus','truck']:
                cls = 'vehicle'
            elif cls in ['其他标志','指示标志','指路标志','禁令标志','警告标志','辅助标志']:
                cls = 't_sign'

            # if cls in ['Red', 'RedLeft', 'RedRight']:
            #     cls = 'tl_red'
            #
            # elif cls in ['Yellow']:
            #     cls = 'tl_yellow'
            # 
            # elif cls in ['off']:
            #     cls = 'tl_none'
            # 
            # elif cls in ['Green', 'GreenLeft', 'GreenRight']:
            #     cls = 'tl_green'

            # print(cls)
            if cls in labels_list:
                # print(cls)
                # print(object.findall("rectangle"))
                bndbox_and_rect = object.findall("rectangle") + object.findall("bndbox")

                for rect in bndbox_and_rect:
                    # print(rect)
                    # if cls=='tl_green':
                    #     g_nums += 1
                    # if cls=='tl_red':
                    #     r_nums += 1
                    # if cls=='tl_yellow':
                    #     y_nums += 1
                    # if cls=='tl_none':
                    #     n_nums += 1

                    labels_nums += 1
                    xmin = float(rect.findall("xmin")[0].text)
                    xmax = float(rect.findall("xmax")[0].text)
                    ymin = float(rect.findall("ymin")[0].text)
                    ymax = float(rect.findall("ymax")[0].text)
                    if xmin < 0:
                        xmin = 0
                    if xmax < 0:
                        xmax = 0
                    if ymin < 0:
                        ymin = 0
                    if ymax < 0:
                        ymax = 0
                    xcenter = (xmin + xmax) /2 / w
                    ycenter = (ymin + ymax) / 2 / h
                    rect_w = (xmax - xmin) / w
                    rect_h = (ymax -ymin) / h
                    # print(xcenter,ycenter,rect_w,rect_h)
                    res += str(labels_list.index(cls))+' '+str(xcenter)+" "+str(ycenter)+" "+str(rect_w)+" "+str(rect_h)+"\n"
                    # print(xmin,xmax,ymin,ymax)
                    # print("="*10)
        # print("##",res)
        return res

    except:
        writeTxt("error_xml.txt",file.split('t\\')[1]+'\n')
def writeXml2Xml(file,newFile):
    print("="*5,file,"="*5)
    with open(file,'r',encoding='utf-8') as f:
        contentLines = f.readlines()
        contents = "".join(contentLines)
    pat = r'encoding="utf-8"\?>\n(.*?)</annotation>'
    # print(re.findall(r'encoding="utf-8"?>(.*)','xcs,is a gooannotationsadas man\nxcs annotationssssad annotation',re.S))
    re_pat = re.compile(pat,re.S)
    # print(contents)
    # data = re.findall(pat,contents,flags=re.S)
    # print(data)
    # print(len(data))
    data = re_pat.findall(contents)
    print(len(data))
    with open(newFile, 'w', encoding='utf-8') as f:
        f.write(data[0]+'</annotation>')

def write_Error_Txt(file,data):
    i = 0
    while os.path.isfile(file):
        t  = file.split(".txt")[0]+"_"+str(i)+".txt"
        file = t
    with open(file,'a') as f:
        f.write(data)

def writeTxt(file,data):
    with open(file,'a') as f:
        f.write(data)

def copyImg(source,dest):
    temple = source.replace(".xml",".jpg")
    img_path = temple.replace("xml",'images')
    # print(img_path)
    shutil.copy(img_path,dest)

if __name__ == '__main__':
    xml_path_ = r'/data/xiaochaosui/dataset/2-new/voc_obj_xml'
    # xml_path = r'D:\xcsy\dataset\traffic_light\test'
    # txt_path = r'D:\xcsy\dataset\traffic_light\labels'
    txt_path = r'/data/xiaochaosui/dataset/2-new/labels'
    # imgs_path = r'D:\xcsy\dataset\data_all\traffic_light\Tl_train_new\Output_final\images'
    mkdir(txt_path)
    # xml_red = r'C:\Users\chaosuix\Downloads\tl_red\xml'
    # xml_yellow = r'C:\Users\chaosuix\Downloads\tl_yellow\xml'
    # xml_green = r'C:\Users\chaosuix\Downloads\tl_green\xml'
    # xml_none = r'C:\Users\chaosuix\Downloads\tl_none\xml'

    # xml_paths = [xml_red,xml_yellow,xml_green,xml_none]
    xml_paths = [xml_path_]
    # print(xml_paths)
    c = 0
    em = 0
    for xml_path in xml_paths:
        xmlsName = os.listdir(xml_path)
        for xmlName in xmlsName:
            name = xmlName.split(".xml")[0]
            # print(name)
            # break
            xmlFile = os.path.join(xml_path,xmlName)
            # try:
            #     tree = ET.parse(xmlFile)
            #     root = tree.getroot()
            # except:
            #     writeTxt("error_xml_car.txt", xmlFile.split('t\\')[1] + '\n')
            # newXmlFile = os.path.join(new_xml_path,xmlName)
            # print(newXmlFile)
            # writeXml2Xml(xmlFile,newXmlFile)

            txt_data = readXml(xmlFile)
            print(txt_data)
            if txt_data ==None or txt_data=="":
                writeTxt("emptyXML.txt",xmlName+"\n")
                em += 1
            txtFile = os.path.join(txt_path,name+".txt")
            # if txt_data != None:
            writeTxt(txtFile, txt_data)
            #     copyImg(xmlFile,imgs_path)
            c += 1



    print('img_nums:',c)
    print('labels_nums',labels_nums)
    # print('g_nums', g_nums)
    # print('y_nums', y_nums)
    # print('r_nums', r_nums)
    # print('n_nums', n_nums)
    data_nums = 'img_nums:'+ str(c) + '\n'\
    'labels_nums:'+ str(labels_nums) + '\n'\
                # 'g_nums:'+ str(g_nums)+ '\n'\
                # 'y_nums:' + str(y_nums)+ '\n'\
                # 'r_nums:' +str(r_nums)+ '\n'\
                # 'n_nums:'+ str(n_nums)+ '\n\n\n\n'
    writeTxt("label_nums.txt",data_nums)
    print("empty xml:",em)



