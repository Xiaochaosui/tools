# @Author:xiaochaosui
# @Organization:FiberHome
# @Email:chaosuixiao@gmail.com
# @Time:2021/11/9 16:53
import os
dir = r"D:\xcsy\code\multi_model_inference\weights"
file_names = os.listdir(dir)
for name in file_names:
    print(name)
    index = name.find("_1")
    new_name = name[:index] + ".pt"
    os.rename(os.path.join(dir,name),os.path.join(dir,new_name))
    print(new_name)
    print(index)
