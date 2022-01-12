import os
import shutil
import cv2

def find_txt(root, out):
    root = root + r'Annotations'
    out = out + r'Annotations'
    txt_names = os.listdir(root)
    n = 0
    for txt_name in txt_names:
        txt_path = root + txt_name
        with open(txt_path) as f:
            lines = f.readlines()[1:]
            for line in lines:
                if line[0] not in classes:
                    continue
                else:
                    n += 1
                    print("{}/{} 找到文档{}".format(n, len(txt_names), txt_name))
                    shutil.copy(txt_path, out)
                    break


def copy_image(root, out):
    txt_path = out + r'Annotations/'
    txt_names = os.listdir(txt_path)
    out = out + r'images/'
    for txt_name in txt_names:
        image_name = txt_name[:-4]
        image_path = root + r'Images/' + image_name
        shutil.copy(image_path, out+image_name)


def convert(size, box):  # size:(原图w,原图h) , box:(xmin,xmax,ymin,ymax)
    dw = 1. / size[0]  # 1/w
    dh = 1. / size[1]  # 1/h
    x = (box[0] + box[1]) / 2.0  # 物体在图中的中心点x坐标
    y = (box[2] + box[3]) / 2.0  # 物体在中的中心点y坐标
    w = box[1] - box[0]  # 物体实际像素宽度
    h = box[3] - box[2]  # 物体实际像素高度
    x = x * dw  # 物体中心点x的坐标比(相当于 x/原图w)
    w = w * dw  # 物体宽度的宽度比(相当于 w/原图w)
    y = y * dh  # 物体中心点y的坐标比(相当于 y/原图h)
    h = h * dh  # 物体宽度的宽度比(相当于 h/原图h)
    return x, y, w, h  # 返回 相对于原图的物体中心点的x坐标比,y坐标比,宽度比,高度比,取值范围[0-1]


def get_img_shape(img_file):
    img = cv2.imread(img_file)
    return img.shape[0], img.shape[1]


def convert_annotation(w, h, root, image_id):
    in_file = open(root + r'Annotations/{}.jpg.txt'.format(image_id), encoding='utf-8')
    out_file = open(root + r'labels/{}.txt'.format(image_id), 'w', encoding='utf-8')

    for line in in_file.readlines()[1:]:
        res = line.split(' ')
        if res[0] not in classes:
            continue
        else:
            b = (float(res[1]), float(res[3]), float(res[2]), float(res[4][:-1]))
            b1, b2, b3, b4 = b
            # 标注越界修正
            if b2 > int(w):
                b2 = int(w)
            if b4 > int(h):
                b4 = int(h)
            b = (b1, b2, b3, b4)
            bb = convert((w, h), b)
            # 生成 calss x y w h 在label文件中
            out_file.write(str(0) + " " + " ".join([str(a) for a in bb]) + '\n')

if __name__ == '__main__':
    classes = ['2']  # 查找类别
    root_path = r'/raid/zhangziyi/dataset/Rider/rider_person/'  # txt文档的根目录
    # out_path = r'D:\1Data\rider\test\result/'  # 输出根目录

    # find_txt(root_path, out_path)
    # copy_image(root_path, out_path)

    for image_id in os.listdir(root_path+r'Annotations/'):
        image = root_path + r'images/' + image_id[:-4]
        h, w = get_img_shape(image)
        image_id_1 = image_id[:-8]
        convert_annotation(w, h, root_path, image_id_1)
