# @Author:xiaochaosui
# @Organization:FiberHome
# @Email:chaosuixiao@gmail.com
# @Time:2021/12/6 10:29

import cv2
import random
import os
import xml.etree.cElementTree as xml_tree
from pathlib import Path
def plot_1_box(x, img, color=None, label=None, line_thickness=None):
    # Plots one bounding box on image img
    tl = line_thickness or round(0.002 * (img.shape[0] + img.shape[1]) / 2) + 1  # line/font thickness
    color = color or [random.randint(0, 255) for _ in range(3)]
    c1, c2 = (int(x[0]), int(x[1])), (int(x[2]), int(x[3]))
    cv2.rectangle(img, c1, c2, color, thickness=tl, lineType=cv2.LINE_AA)
    if label:
        tf = max(tl - 1, 1)  # font thickness
        t_size = cv2.getTextSize(label, 0, fontScale=tl / 3, thickness=tf)[0]
        c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
        cv2.rectangle(img, c1, c2, color, -1, cv2.LINE_AA)  # filled
        cv2.putText(img, label, (c1[0], c1[1] - 2), 0, tl / 3, [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)

def plot_img(img_path,xml_path,save_path):
    # img_formats = ['bmp', 'jpg', 'jpeg', 'png', 'tif', 'tiff', 'dng', 'webp', 'mpo']
    print("=" * 5 + " Plot BBox " + "=" * 5)
    xml_files = os.listdir(xml_path)
    random.seed(10)
    colors = [[random.randint(0, 255) for _ in range(3)] for _ in range(30)]
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    # print(xml_files)
    weights = {}
    i = 0
    img_names = os.listdir(img_path)
    for img_name in img_names:
        ID = 0
        file_name = Path(img_name).stem
        print("file_name:",file_name)
        # print(file_name)
        img_file = os.path.join(img_path,img_name)
        save_img = os.path.join(save_path,img_name)
        xml_file = os.path.join(xml_path,file_name+".xml")
        print(img_file)
        img = cv2.imread(img_file)
        tree = xml_tree.parse(os.path.join(xml_path,xml_file))
        root = tree.getroot()
        objects = root.findall("object")
        for obj in objects:
            cls = obj.findall("name")[0].text.capitalize()
            ID +=1

            # conf = obj.findall("conf")[0].text
            label = '%s %s' % (cls,str(ID))
            bndbox_and_rect = obj.findall("rectangle") + obj.findall("bndbox")
            rect = bndbox_and_rect[0]
            xmin = float(rect.findall("xmin")[0].text)
            xmax = float(rect.findall("xmax")[0].text)
            ymin = float(rect.findall("ymin")[0].text)
            ymax = float(rect.findall("ymax")[0].text)
            x= [xmin, ymin, xmax, ymax]
            # print(label)
            if cls not in weights.keys():
                weights[cls] = i
                i+=1
            # print("colors:",len(colors))
            # print("weights:", len(weights))
            # print("cls:", cls)
            # if cls == "rider".capitalize():
            #     plot_1_box(x,img,colors[int(weights[cls])],label,line_thickness=2)
            plot_1_box(x, img, colors[int(weights[cls])], label, line_thickness=2)

        cv2.imwrite(save_img, img)
    print("labels:",weights)


# img(cv2 已读) 和xml绝对路径
def plot_one_img(img,xml_file,save_img_file):
    random.seed(10)
    colors = [[random.randint(0, 255) for _ in range(3)] for _ in range(30)]
    weights = {}
    tree = xml_tree.parse(xml_file)
    root = tree.getroot()
    objects = root.findall("object")
    i = 0
    for obj in objects:
        cls = obj.findall("name")[0].text.capitalize()
        ID = obj.findall("ID")
        if ID:
            ID = obj.findall("ID")[0].text
            label = '%s %s' % (cls, ID)
        else:
            label = '%s' % (cls)
        bndbox_and_rect = obj.findall("rectangle") + obj.findall("bndbox")
        rect = bndbox_and_rect[0]
        xmin = float(rect.findall("xmin")[0].text)
        xmax = float(rect.findall("xmax")[0].text)
        ymin = float(rect.findall("ymin")[0].text)
        ymax = float(rect.findall("ymax")[0].text)
        x = [xmin, ymin, xmax, ymax]
        if cls not in weights.keys():
            weights[cls] = i
            i += 1
        plot_1_box(x, img, colors[int(weights[cls])], label, line_thickness=2)

    cv2.imwrite(save_img_file, img)
    print("labels:", weights)
    return save_img_file


if __name__ == '__main__':
    img_path = r"/data/xiaochaosui/dataset/all_person/face_images_output/face_out/JPEGImages"
    xml_path = r"/data/xiaochaosui/dataset/all_person/face_images_output/face_out/Annotations"
    save_path = r"/data/xiaochaosui/dataset/all_person/face_images_output/face_out/new"
    plot_img(img_path,xml_path,save_path)