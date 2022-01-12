# @Author:xiaochaosui
# @Organization:FiberHome
# @Email:chaosuixiao@gmail.com
# @Time:2021/12/15 14:32


import os
from pathlib import Path
import cv2
import shutil
from tools import  mkdir
if __name__ == '__main__':
    image_input_path = Path(r"D:\xcsy\dataset\data_all\rider\rider_train_final\roi_rider\rider") # 总的小目标
    image_output_path_0 = Path(r"D:\xcsy\dataset\data_all\rider\rider_train_final\roi_rider\rider_0") # 留着的
    image_output_path_1 = Path(r"D:\xcsy\dataset\data_all\rider\rider_train_final\roi_rider\rider_1") # 不要的
    mkdir(image_output_path_0)
    mkdir(image_output_path_1)
    image_names = os.listdir(image_input_path)
    for image_name in image_names:
        img_file = image_input_path / image_name
        print(img_file)
        image_output_file_0 = image_output_path_0 / image_name
        image_output_file_1 = image_output_path_1 / image_name
        img = cv2.imread(str(img_file))
        h,w,c= img.shape
        print(img.shape)
        # print(type(h))
        if h>=20 and w >=20 and h*w>=600 :
        # if h>=30 and w>=10 and h*w>=380:
            shutil.copy(str(img_file),str(image_output_file_1))
        else:
            shutil.copy(str(img_file), str(image_output_file_0))



