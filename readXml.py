# @Author:xiaochaosui
# @Organization:FiberHome
# @Email:chaosuixiao@gmail.com
# @Time:2021/12/2 9:04
import xml.etree.ElementTree as ET
import math
from plot_box import plot_img
def p2p_distance(p1,p2):
    x1 = p1[2][0]
    y1 = p1[2][1]
    x2= p2[2][0]
    y2 = p2[2][1]
    res = math.sqrt((x1-x2) ** 2 + (y1-y2) **2)
    return res
def p2p_compare_litte(p1,p2):
    if p1[1] < p2[1]:
        return p1[0]
    else:
        return p2[0]


# 剔除的矩形框
def readXml_del_rect(file):
    print("="*5,file,"="*5)
    try:
        tree = ET.parse(file)
        root = tree.getroot()
        w = int(root.findall("size")[0].findall("width")[0].text)
        h = int(root.findall("size")[0].findall("height")[0].text)
        res = ''
        print("$$$",len(root.findall("object")))
        arrow_p = {}
        for obj in root.findall("object"):
            cls = obj.findall("class")[0].text.capitalize()
            conf = obj.findall("conf")[0].text
            if "Arrow" in cls:
                for rect in obj.findall("rectangle"):
                    xmin = int(rect.findall("xmin")[0].text)
                    xmax = int(rect.findall("xmax")[0].text)
                    ymin = int(rect.findall("ymin")[0].text)
                    ymax = int(rect.findall("ymax")[0].text)
                    x = [xmin,ymin]
                    # x = [(xmin+xmax)/2,(ymin+ymax)/2]
                    ID = obj.findall("ID")[0].text
                    if cls not in arrow_p.keys():
                        arrow_p[cls] = [[ID,float(conf),x]]
                    else:
                        arrow_p[cls].append([ID,float(conf), x])

                print(cls,conf,x)
        print(arrow_p)
        i = 0
        arrow_p_keys = list(arrow_p.keys())
        # print(arrow_p_keys)
        e = 10
        keys_num = len(arrow_p_keys)
        min_ids = []
        min1 = 9999
        for k_b in arrow_p_keys:

            i +=1
            if i >= keys_num:
                break
            for k in arrow_p_keys[i:]:

                 for p1 in arrow_p[k_b]:
                     for p2 in arrow_p[k]:
                        distance = p2p_distance(p1,p2)
                        if distance <= e:
                            del_id = p2p_compare_litte(p1,p2)
                            del_obj(root,del_id)
                            min_ids.append(del_id)
                            print("min")
                        print(distance)
        tree.write(file, encoding='utf-8')
        print("剔除的点:",min_ids)
    except Exception as e:
        print("error_xml.txt",file.split('t\\')[1]+'\n')
        print(e)

def del_obj(root,del_ID):
    for obj in root.findall("object"):
        ID = obj.findall("ID")[0].text
        if ID == del_ID:
            root.remove(obj)

# 获得xml的所有obj
def xml_get_object(file):
    print("=" * 5, file, "=" * 5)
    tree = ET.parse(file)
    root = tree.getroot()
    objs = root.findall("object")
    return objs

# 获得obj 矩形框
def xml_get_rect(obj):
    x = []
    try:
        rect = obj.findall("rectangle")[0]
        xmin = int(rect.findall("xmin")[0].text)
        xmax = int(rect.findall("xmax")[0].text)
        ymin = int(rect.findall("ymin")[0].text)
        ymax = int(rect.findall("ymax")[0].text)
        x = [xmin, ymin,xmax,ymax]
    except Exception as e:
        print("xml_get_rect Error:" + e)

    return x

# 获得xml的指定类别和矩形框
def xml_get_rect(obj,label):
    x = []
    try:
        cls = obj.findall(label)[0].text.capitalize()
        if cls == label:
            rect = obj.findall("rectangle")[0]
            xmin = int(rect.findall("xmin")[0].text)
            xmax = int(rect.findall("xmax")[0].text)
            ymin = int(rect.findall("ymin")[0].text)
            ymax = int(rect.findall("ymax")[0].text)
            x = [xmin, ymin,xmax,ymax]
    except Exception as e:
        print("xml_get_rect Error:" + e)

    return cls,x


if __name__ == '__main__':
    xml_file = r"D:\xcsy\245_246\detect\0_test\All_Results\All_Annotations\WIN_20210618_16_06_38_Pro_2805.xml"
    readXml_del_rect(xml_file)
    img_path = r"D:\xcsy\245_246\detect\0_test\All_Results\img"
    xml_path = r"D:\xcsy\245_246\detect\0_test\All_Results\All_Annotations"
    save_path = r"D:\xcsy\245_246\detect\0_test\All_Results\new"
    plot_img(img_path, xml_path, save_path)