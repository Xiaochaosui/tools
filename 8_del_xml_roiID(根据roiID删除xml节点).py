# @Author:xiaochaosui
# @Organization:FiberHome
# @Email:chaosuixiao@gmail.com
# @Time:2021/12/13 16:16


from tools import xml_get_object,del_roi_obj,mkdir
from pathlib import Path
import os
if __name__ == '__main__':
    root_path = Path(r"D:\xcsy\dataset\data_all\rider\rider_train_final") # 根目录

    bad_roi_path = root_path / r"bad_img" # bad小目标 需要被删除的小目标
    xml_path = root_path / r"Annotations" # 输入的xml
    bad_out_xml_path = root_path /r"xml_bad" # 改变得 输出的xml
    label_roi = "rider"

    mkdir(bad_out_xml_path)
    bad_roi_names = os.listdir(bad_roi_path)
    for bad_roi_name in bad_roi_names:

        bad_roi_file = bad_roi_path / bad_roi_name
        file_formate = bad_roi_file.suffix # img 文件格式
        temple = bad_roi_name.split("_")
        # file_name = bad_roi_file.stem # 文件名字 不带后缀的
        file_name = "_".join(temple[:-1])
        print("file_name:", file_name)
        xml_file = xml_path / (file_name + ".xml")
        xml_out_file = bad_out_xml_path / (file_name + ".xml")
        roi_id = temple[-1].split(".")[0]
        print("xml_file:",xml_file)
        print("bad_roi_file:",bad_roi_file)
        print("roi_id:",roi_id)
        tree,root,objects = xml_get_object(xml_file)
        del_roi_obj(root,roi_id,label_roi)
        print("改变的xml:", xml_file)
        tree.write(xml_out_file, encoding='utf-8')


