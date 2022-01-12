# @Author:xiaochaosui
# @Organization:FiberHome
# @Email:chaosuixiao@gmail.com
# @Time:2021/12/6 13:43
import os
import cv2
from plot_box import plot_1_box
import random
from tools import  mkdir
def get_rect(file):
    res = []
    with open(file) as f:
        data = f.readlines()
        w = 648
        h = 480
        for line in data:
            temple = []
            data_line = line.split(" ")
            cls = data_line[0]
            for x in data_line[1:]: #cx,cy,rw,rh
                temple.append(float(x))
            res.append(center2xy(temple,w,h))
        # print("res:",res)
    return res,cls


def center2xy(c,w,h):
    cx = c[0]
    cy = c[1]
    r_w = c[2]
    r_h = c[3]
    xmin = (2*w*cx-r_w*w)/2
    xmax = (2*w*cx+r_w*w)/2
    ymin = (2*h*cy-r_h*h)/2
    ymax = (2 * h * cy + r_h * h) / 2
    return [xmin,ymin,xmax,ymax]




if __name__ == '__main__':
    txt_path = r"D:\xcsy\dataset\data_all\rider\rider_wider\labels"
    txtNames = os.listdir(txt_path)
    # res = read_txt("person_nums.txt")
    # print(res)
    img_path = r"D:\xcsy\dataset\data_all\rider\rider_wider\images"
    img_out_path = r"D:\xcsy\dataset\data_all\rider\rider_wider\Images_box"
    mkdir(img_out_path)
    colors = [[0,255,0],[0,0,255],[random.randint(0, 255) for _ in range(3)],[random.randint(0, 255) for _ in range(3)]]
    for txtName in txtNames:
        name = txtName.split(".txt")[0]
        imgFile = os.path.join(img_path, name+".jpg")
        txtFile = os.path.join(txt_path, txtName)
        imgFile_out = os.path.join(img_out_path, name + ".jpg")
        print(imgFile)
        print(txtFile)
        img = cv2.imread(imgFile)
        rect,cls = get_rect(txtFile)
        for x in rect:
            plot_1_box(x,img,colors[int(cls)],line_thickness=1)
        cv2.imwrite(imgFile_out, img)
        print(rect)


