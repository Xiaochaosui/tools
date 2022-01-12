import os
import shutil

root = r'D:\xcsy\dataset\face\all_to_/'  # 根目录
label_path = r'labels'  # 需要过滤的label路径
image_path = r'images'  # 需要过滤的image路径

label_out_path = root + label_path + '_out_2'
image_out_path = root + image_path + '_out_2'


if not os.path.isdir(label_out_path):
    os.makedirs(label_out_path)
if not os.path.isdir(image_out_path):
    os.makedirs(image_out_path)

n = 0
for label in os.listdir(root+label_path):
    lab = os.path.join(root+label_path, label)
    image = os.path.join(root+image_path, label[:-4]+'.jpg')
    flag = 0
    if not os.path.isfile(image):
        image = os.path.join(root + image_path, label[:-4] + '.png')
        flag = 1
    if not os.path.isfile(image):
        image = os.path.join(root + image_path, label[:-4] + '.jpeg')
        flag = 1

    if os.path.getsize(lab) != 0:
        n += 1
        shutil.copy(lab, os.path.join(label_out_path, label))
        if flag == 1:
            shutil.copy(image, os.path.join(image_out_path, label[:-4]+'.png'))
        else:
            shutil.copy(image, os.path.join(image_out_path, label[:-4] + '.jpg'))

print("一共有{}个".format(n))
