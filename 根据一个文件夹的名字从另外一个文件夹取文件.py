# @Author:xiaochaosui
# @Organization:FiberHome
# @Email:chaosuixiao@gmail.com
# @Time:2021/12/10 14:41
import os
import shutil
from tools import mkdir
if __name__ == '__main__':
    # xml_path = r'D:\xcsy\dataset\data_all\traffic_light\Tl_train_new\Annotations'
    # txt_path = r'D:\xcsy\dataset\data_all\traffic_light\Tl_train_new\labels_out_2'
    # xml_out_path = r"D:\xcsy\dataset\data_all\traffic_light\Tl_train_new\Annotations_2"
    # mkdir(xml_out_path)
    # 需要挑的文件
    img_old_path = r"D:\xcsy\245_246\detect\rider_detect\rider_infer_image\JPEGImages"
    # 被挑的文件池
    img_new_path = r"D:\xcsy\dataset\data_all\rider\rider_train_final\roi_rider\rider"
    # 挑出来放的位置
    img_out_path = r"D:\xcsy\dataset\data_all\rider\rider_train_final\roi_rider\roi_rider_final"
    imgNames = os.listdir(img_old_path)
    print(len(imgNames))

    for imgName in imgNames:
        imgFile_old = os.path.join(img_new_path, imgName)
        imgFile_new_out = os.path.join(img_out_path, imgName)
        if not os.path.isfile(imgFile_new_out):
            print(imgFile_old)
            print(imgFile_new_out)
            shutil.copy(imgFile_old, imgFile_new_out)



