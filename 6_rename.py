# @Author:xiaochaosui
# @Organization:FiberHome
# @Email:chaosuixiao@gmail.com
# @Time:2021/12/3 10:39

import os
from pathlib import Path
if __name__ == '__main__':
    path = r"D:\xcsy\dataset\data_all\traffic_light\changed_增广\Annotations"  # 只要换这里 图片的路径
    file_names = os.listdir(path)
    n=1
    for name in file_names:
        img_formate = Path(name).suffix
        img_name = Path(name).stem
        print(img_name,img_formate)
        new_name = img_name+"_"+str(n) + img_formate
        n+=1
        os.rename(os.path.join(path, name), os.path.join(path, new_name))
        print(new_name)
#