# @Author:xiaochaosui
# @Organization:FiberHome
# @Email:chaosuixiao@gmail.com
# @Time:2021/12/1 16:17
import cv2
import random
import  xml.etree.cElementTree as xml_tree
import os
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
    img_formate = img_names[0].rsplit(".",1)[-1]
    for xml_file in xml_files:
        file_name = xml_file.rsplit(".",1)[0]
        # print(file_name)
        img_file = os.path.join(img_path,file_name+'.'+img_formate)
        save_img = os.path.join(save_path,file_name+'.'+img_formate)
        print(img_file)
        img = cv2.imread(img_file)


        tree = xml_tree.parse(os.path.join(xml_path,xml_file))
        root = tree.getroot()
        objects = root.findall("object")
        for obj in objects:
            cls = obj.findall("class")[0].text.capitalize()
            label = '%s' % (cls)
            for rect in obj.findall("rectangle"):
                xmin = int(rect.findall("xmin")[0].text)
                xmax = int(rect.findall("xmax")[0].text)
                ymin = int(rect.findall("ymin")[0].text)
                ymax = int(rect.findall("ymax")[0].text)
                x= [xmin, ymin, xmax, ymax]
            # print(label)
            if cls not in weights.keys():
                weights[cls] = i
                i+=1
            # print("colors:",len(colors))
            # print("weights:", len(weights))
            # print("cls:", cls)
            plot_1_box(x,img,colors[int(weights[cls])],label,line_thickness=2)
        print(save_img)
        cv2.imshow("x",img)
        cv2.waitKey()
        cv2.imwrite(save_img, img)
    print("labels:",weights)

if __name__ == '__main__':
    img_file = r""
    source = r"D:\xcsy\dataset\test_add_rect\image" # 原图路径 路径不能有中文
    xml_path = r"D:\xcsy\dataset\test_add_rect\xml" #xml路径
    output = r"D:\xcsy\dataset\test_add_rect\output"    #拉好框的图的路径
    if not os.path.exists(output):
        os.makedirs(output)
    plot_img(source, xml_path, output)