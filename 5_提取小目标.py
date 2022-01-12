# @Author:xiaochaosui
# @Organization:FiberHome
# @Email:chaosuixiao@gmail.com
# @Time:2021/12/9 15:30


from tools import xml_get_rect,xml_get_object,extract_ROI,mkdir,find_rect_W_h,CreateObjElem
import cv2
import os
import codecs
import xml.dom.minidom
from pathlib import Path
if __name__ == '__main__':

    root_path = r"D:\xcsy\dataset\data_all\rider\rider_train_final" # 根目录
    imgs_path = os.path.join(root_path,'images') # 图片输入
    xml_test = os.path.join(root_path,'Annotations')  # xml输入

    img_out_path = os.path.join(root_path,'roi_rider') # 小目标输出
    xml_out_path = os.path.join(root_path,'xml_out_roiID') # xml输出 会增加一个roi_ID节点

    temple_path = r'D:\xcsy\dataset\data_all\Person\person_myself\roi_person_W_h' # 图片大小为 W大于h的文件夹
    # mkdir(temple_path)


    mkdir(xml_out_path)
    label_names = {"rider":0} # 需要提取的小目标name, k:v-> 类别:数量,数量初始化都是0

    # label_names = {'tl_green':0,'tl_red':0,'tl_yellow':0,'tl_none':0}
    xml_paths = [xml_test] # 可以放多个xml文件夹
    xml_file_list = []
    print("xml_path:",xml_paths)
    for xml_path in xml_paths:
        # if xml_path == xml_test_path:
        #     imgs_path = r'D:\xcsy\dataset\data_all\traffic_light\Tl_bstld_test\test'
        # else:
        #     imgs_path = r'D:\xcsy\dataset\data_all\traffic_light\TL_bstld_train\images'

        xml_names = os.listdir(xml_path)
        imgs_name = os.listdir(imgs_path)

        for xml_name in xml_names:
            flag_xml = 0
            xml_file = os.path.join(xml_path,xml_name)
            file_name = Path(xml_name).stem
            # print("file_name",file_name)
            xml_out_file = os.path.join(xml_out_path,xml_name)
            img_name = file_name + ".jpg"
            img_file = os.path.join(imgs_path,img_name)
            flag = 0
            if not os.path.isfile(img_file):
                img_name = file_name + ".png"
                img_file = os.path.join(imgs_path,img_name)
                flag = 1
            if not os.path.isfile(img_file):
                img_name = file_name + ".jpeg"
                img_file = os.path.join(imgs_path,img_name)
                flag = 1

            print("img_file:",img_file)
            img = cv2.imread(img_file)
            tree,root,objs = xml_get_object(xml_file)
            rect_n = 0
            for obj in objs:
                cls = obj.findall("name")[0].text

                if cls in label_names.keys():
                    for label_name in label_names.keys():
                        if cls==label_name:
                            roi_img_path = os.path.join(img_out_path, cls)
                            label_names[cls] += 1
                            mkdir(roi_img_path)

                    rect = xml_get_rect(obj)
                    # print(rect)
                    if len(rect) != 0:
                        # rect_W_h = find_rect_W_h(rect, obj)
                        rect_W_h = False # 是否需要找出小目标中 W大于H的
                        roi_img = extract_ROI(img,rect)
                        if rect_W_h == True:
                            # cv2.imshow("X",roi_img)
                            # cv2.waitKey()
                            flag_xml = 1
                            rect_n += 1
                            roi_img_file = os.path.join(temple_path, file_name + "_" + str(rect_n) + ".jpg")
                            print("roi_file_W_h:", roi_img_file)
                            cv2.imwrite(roi_img_file, roi_img)
                            continue
                    else:
                        continue


                    roi_ID = obj.findall("roi_ID") # 文件名的_最后一位是 roi区域的ID 最后可以根据这个来删除xml信息
                    if roi_ID:
                        roi_ID[0].text = str(rect_n)
                        roi_ID_ = rect_n
                    else:
                        roi_ID_ = rect_n
                        print("$$$4",obj.text)
                        CreateObjElem(obj,"roi_ID",str(roi_ID_))
                    roi_img_file = os.path.join(roi_img_path, file_name+"_"+str(roi_ID_)+".jpg")
                    rect_n += 1
                    print("roi_file:",roi_img_file)
                    cv2.imwrite(roi_img_file,roi_img)
            if flag_xml==1:
                print("改变的xml:",xml_file)
                xml_file_list.append(xml_out_file)
            # print("$$4",xml_out_file)
            tree.write(xml_out_file, encoding='utf-8')
            # 修改格式
            # DomTree = xml.dom.minidom.parse(xml_out_file)
            # annotation1 = DomTree.documentElement
            # f = codecs.open(xml_out_file, 'w', 'utf-8')
            # annotation1.writexml(f, addindent='    ', newl="\n")

    print("改变的xml:",xml_file_list)
    print('label_nums', label_names)


