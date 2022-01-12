# @Author:xiaochaosui
# @Organization:FiberHome
# @Email:chaosuixiao@gmail.com
# @Time:2021/12/31 15:33


import os
from pathlib import Path
import cv2
from tools import mkdir
if __name__ == '__main__':
    img_path = r"D:\xcsy\dataset\data_all\rider\rider_train_final\roi_rider\rider_1"
    image_output_path_0 = Path(r"D:\xcsy\dataset\data_all\rider\rider_train_final\roi_rider\rider_1_resize")
    image_names = os.listdir(img_path)
    mkdir(image_output_path_0)
    for image_name in image_names:
        img_file = Path(img_path) / image_name
        print(img_file)
        image_output_file_0 = image_output_path_0 / image_name
        img = cv2.imread(str(img_file))
        # cv2.imshow("a",img)
        # cv2.waitKey()
        img_ = cv2.resize(img,(88,189),cv2.INTER_LANCZOS4)
        # print(image_output_file_0)
        cv2.imwrite(str(image_output_file_0),img_)
        # break