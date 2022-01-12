# @Author:xiaochaosui
# @Organization:FiberHome
# @Email:chaosuixiao@gmail.com
# @Time:2021/11/25 11:00

import os
import shutil
from encoder import encode_txt



def copy_img(img_path_all,img_path_son,img_path_new):
    imgs = os.listdir(img_path_son)
    for x in imgs:
        img_old = os.path.join(img_path_all,x)
        img_new = os.path.join(img_path_new, x)
        shutil.copy(img_old,img_new)


def build_stand_file(img_root):
    for i in range(1, 5):
        img_path_new = os.path.join(img_root,str(i))
        if not os.path.isdir(img_path_new):
            os.makedirs(img_path_new)
        xml_path_new = os.path.join(img_path_new,"xml_"+str(i))
        xml_path_old = os.path.join(img_root,"Annotations/xml_"+str(i))
        img_path_new = os.path.join(img_path_new, "img_" + str(i))
        img_path_old = os.path.join(img_root, "JPEGImages/img_" + str(i))
        try:
            shutil.copytree(xml_path_old,xml_path_new)
            shutil.copytree(img_path_old, img_path_new)
        except :
            print("文件目录 "+xml_path_new+"&"+img_path_new+" 已存在")


if __name__ == '__main__':
    # 生成的是1-4个 各种分布的xml和img以及供标注软件打开的output
    # 为了更方便使用 代码 我把 目录结构统一化 和 加密xml代码都放到一块了，只需要改下面这两个路径就可以
    # 两个路径的注释说明了 怎么填
    img_path_all = r"D:\xcsy\245_246\挑数据\2\BF_000" # 原生 图片路径
    img_root = r"D:\xcsy\245_246\挑数据\2\Tl\\"  # 推理完的图片和xml根目录 注意最后的双斜杠必须要



    build_stand_file(img_root)  # 统一目录结构
    # 从原图中copy被挑选之后的未拉框的原图 用于标注软件打开
    for i in range(1,5):
        img_path_son = img_root+ str(i) + r"\img_"+str(i)
        img_path_new = img_root+str(i)+"\img"
        if not os.path.isdir(img_path_new):
            os.makedirs(img_path_new)
        copy_img(img_path_all,img_path_son,img_path_new)
        root = img_root + str(i)  # 图片和xml的根目录
        input_obj_xml = root + '/xml_' + str(i) + '/'  # 输入需要加密的的xml目录
        output_obj_txt = root + '/output/voc_obj/'  # 这里不用改
        if not os.path.exists(output_obj_txt):
            os.makedirs(output_obj_txt)
        xmllist = os.listdir(input_obj_xml)
        for xml in xmllist:
            image_type = 'jpg'
            image = xml[:-(len(image_type) + 1)] + '.jpg'
            obj_xml_name = input_obj_xml + xml
            encode_txt(obj_xml_name, output_obj_txt, image)