# @Author:xiaochaosui
# @Organization:FiberHome
# @Email:chaosuixiao@gmail.com
# @Time:2021/12/9 9:30
import xml.etree.ElementTree as ET
import math
import os
# 删除指定的ID的obj
def del_obj(root, del_ID):
    for obj in root.findall("object"):
        ID = obj.findall("ID")[0].text
        if ID == del_ID:
            root.remove(obj)

# 删除指定的roi_ID的obj
def del_roi_obj(root, del_ID,label_):
    for obj in root.findall("object"):
        roi_ID_list = obj.findall("roi_ID")
        if roi_ID_list:
            cls = obj.findall("name")[0].text.capitalize()
            roi_id_xml = roi_ID_list[0].text
            if cls == label_.capitalize() and roi_id_xml == del_ID:
                root.remove(obj)

# 获得xml的所有obj
def xml_get_object(file):
    print("=" * 5, file, "=" * 5)
    tree = ET.parse(file)
    root = tree.getroot()
    objs = root.findall("object")
    return tree,root,objs


# 获得obj的矩形框
def  xml_get_rect(obj):
    x = []
    try:
            bndbox_and_rect = obj.findall("rectangle") + obj.findall("bndbox")
            rect = bndbox_and_rect[0]
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
            x = [xmin, ymin, xmax, ymax]
    except Exception as e:
        print("xml_get_rect Error:")
        print(e)

    return x


def extract_ROI(img,rect):
    xmin = int(rect[0])
    ymin = int(rect[1])
    xmax = int(rect[2])
    ymax = int(rect[3])
    # print(img.shape)
    dst = img[ymin:ymax,xmin:xmax]
    return dst

# 创建文件夹
def mkdir(path):
    if not os.path.isdir(path):
        os.makedirs(path)


def find_rect_W_h(rect,obj):
    xmin = rect[0]
    ymin = rect[1]
    xmax = rect[2]
    ymax = rect[3]
    rect_w = xmax-xmin
    rect_h = ymax-ymin
    if rect_w >rect_h:
        obj.findall("name")[0].text = "person_W_h"
        return True
    else:
        return False

# 增加一个xml节点
def CreateObjElem(father_elem, elem_name, elem_text=None):
    elem = ET.Element(elem_name)
    if not elem_text==None:
        elem.text = elem_text
    father_elem.append(elem)

