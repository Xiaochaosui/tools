# @Author:xiaochaosui
# @Organization:FiberHome
# @Email:chaosuixiao@gmail.com
# @Time:2021/12/22 9:25
import os
from tools import xml_get_object
if __name__ == '__main__':
    root_input = r'D:\xcsy\dataset\face\all_to_'  # 输入根目录
    extend = ['face']
    xml_input_path = os.path.join(root_input, 'Annotations')
    n = 0
    for xml_input in os.listdir(xml_input_path):
        xml_input_file = os.path.join(xml_input_path,xml_input)
        tree,root,objs = xml_get_object(xml_input_file)
        for object in objs:
            name = object.findall("name")[0].text
            if name in extend:
                n += 1

        print('已完成{}'.format( xml_input))
    print("faces:",n)