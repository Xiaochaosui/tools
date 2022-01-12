# @Author:xiaochaosui
# @Organization:FiberHome
# @Email:chaosuixiao@gmail.com
# @Time:2021/10/8 14:14


import os
import shutil
from tools import mkdir
def extra_same_elem(l1,l2):
    set1 = set(l1)
    set2 = set(l2)
    res = set1.intersection(l2)
    return list(res)

def list_remove_other(l1,l2):
    return list(set(l1)-set(l2))

def rename(source,dst):

    os.rename(source, dst)


if __name__ == '__main__':
    # path_red = r'D:\xcsy\dataset\tl_red\images'
    # path_yellow = r'D:\xcsy\dataset\tl_yellow\images'
    # path_green = r'D:\xcsy\dataset\tl_green\images'
    # path_none = r'D:\xcsy\dataset\tl_none\images'
    # path_trafficlight =r'D:\xcsy\dataset\traffic_light\images'

    path_1 = r"D:\xcsy\dataset\data_all\rider\rider_train_final\roi_rider\rider"
    path_2 = r"D:\xcsy\dataset\data_all\rider\rider_train_final\roi_rider\roi_rider_final"
    path_3 = r"D:\xcsy\dataset\data_all\rider\rider_orig\images"
    path_4 = r"D:\xcsy\dataset\data_all\rider\rider_wider\images"
    xml_1 = r"D:\xcsy\dataset\data_all\traffic_light\Tl_bstld_test\Annotations"
    xml_2 = r"D:\xcsy\dataset\data_all\traffic_light\bstld\TL_bstld_train\Annotations"

    # same_1 = r"D:\xcsy\dataset\data_all\traffic_light\bstld\same_test"
    # same_2 = r"D:\xcsy\dataset\data_all\traffic_light\bstld\same_train"
    # mkdir(same_1)
    # mkdir(same_2)
    repetion_name = []
    name_1 = os.listdir(path_1)
    name_2 = os.listdir(path_2)
    # name_3 = os.listdir(path_3)
    # name_4 = os.listdir(path_4)
    res1 = extra_same_elem(name_1, name_2)
    print(len(res1))
    res_12 =list_remove_other(name_2,res1)
    print("2-1:",res_12)

    # res2 =extra_same_elem(name_3, res_12)
    #
    # res_32 = list_remove_other(res_12, res2)
    # print("2-1-3:",len(res_32))
    # res3 = extra_same_elem(name_4, res_32)
    # res_42 = list_remove_other(res_32, res3)
    # print("2-1-3-4:", len(res_42))
    # print(res_42)
    # rename同名文件
    # for img_name in res1:
    #     file_name = img_name.split(".")[0]
    #     xml_name = file_name+".xml"
    #     new_xml_name = file_name + "_r.xml"
    #     new_img_name = file_name + "_r.png"
    #
    #     # xml_file_1 = os.path.join(xml_1, xml_name)
    #     xml_file_2 = os.path.join(xml_2, xml_name)
    #     new_xml_file = os.path.join(xml_2, new_xml_name)
    #     rename(xml_file_2,new_xml_file)
    #
    #     img_file_2 = os.path.join(path_2, img_name)
    #     new_img_file = os.path.join(path_2, new_img_name)
    #     rename(img_file_2, new_img_file)
        # dest_1 = os.path.join(same_1,xml_name)
        # dest_2 = os.path.join(same_2, xml_name)

        # shutil.copy(xml_file_1, dest_1)
        # shutil.copy(xml_file_2, dest_2)

    # print(res1)
    # print(len(res1))
    # print(len(res2))
    # red_name = os.listdir(path_red)
    # yellow_name = os.listdir(path_yellow)
    # green_name = os.listdir(path_green)
    # none_name = os.listdir(path_none)
    # trafficlight_name = os.listdir(path_trafficlight)
    #
    # res1 = extra_same_elem(red_name,trafficlight_name)
    # res2 = extra_same_elem(yellow_name, trafficlight_name)
    # res3 = extra_same_elem(green_name, trafficlight_name)
    # res4 = extra_same_elem(none_name, trafficlight_name)
    # print(len(res1))
    # print(len(res2))
    # print(len(res3))
    # print(len(res4))

