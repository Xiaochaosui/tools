# @Author:xiaochaosui
# @Organization:FiberHome
# @Email:chaosuixiao@gmail.com
# @Time:2021/9/27 14:59


import os
import random
def writeData(file,data):
    with open(file,'w') as f:
        for name in data:
            signal_data = '/data/xiaochaosui/dataset/2-new/images/'
            signal_data += name
            # print(signal_data)
            f.write(signal_data+'\n')

def extra_same_elem(l1,l2):
    set1 = set(l1)
    set2 = set(l2)
    res = set1.intersection(l2)
    return list(res)

def list_remove_other(l1,l2):
    return list(set(l1)-set(l2))

if __name__ == '__main__':
    train_scale = 0.9

    val_scale = 0.7
    test_scale = 0.3
    imgs_path = r'/data/xiaochaosui/dataset/2-new/images'
    path = r'/data/xiaochaosui/dataset/2-new/' #存放的根目录
    imgs_name = os.listdir(imgs_path)
    imgs_nums = len(imgs_name)


    train_nums = imgs_nums * train_scale


    # print(imgs_nums,train_nums,val_nums)
    # test = ['xcs','aa','addad','1231']
    random.seed(10)
    train_data = random.sample(imgs_name,round(train_nums))
    val_test_data = list_remove_other(imgs_name,train_data)

    val_nums = len(val_test_data) * val_scale


    val_data =random.sample(val_test_data,round(val_nums))
    test_data = list_remove_other(val_test_data,val_data)

    temple = extra_same_elem(train_data,val_data)
    print(len(temple))

    # print(len(train_data),len(val_data),len(train_data)+len(val_data))
    train_txt = os.path.join(path,'train.txt')
    val_txt = os.path.join(path,'val.txt')
    test_txt = os.path.join(path, 'test.txt')
    print("="*5,"write train_txt","="*5)
    writeData(train_txt,train_data)
    print(len(train_data))
    print("=" * 5, "write val_txt", "=" * 5)
    writeData(val_txt, val_data)
    print(len(val_data))

    print("=" * 5, "write test_txt", "=" * 5)
    writeData(test_txt, test_data)
    print(len(test_data))







