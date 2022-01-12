# @Author:xiaochaosui
# @Organization:FiberHome
# @Email:chaosuixiao@gmail.com
# @Time:2021/12/9 9:12

from tools import xml_get_rect,xml_get_object,extract_ROI,mkdir

import cv2
import os
if __name__ == '__main__':
    xml_train_path =r"D:\xcsy\dataset\data_all\traffic_light\TL_bstld_train\Annotations"
    xml_test_path = r"D:\xcsy\dataset\data_all\traffic_light\Tl_bstld_test\Annotations"

    # xml_names = os.listdir(xml_path)


    g_nums = 0
    y_nums = 0
    r_nums = 0
    n_nums = 0

    imgs_path = r'D:\xcsy\dataset\data_all\traffic_light\Tl_train_new\images_out_2' # 图片输入
    img_out_path = r'D:\xcsy\dataset\data_all\traffic_light\Tl_train_new\roi_2' # 小目标输出
    # img_out_path = r"D:\xcsy\dataset\data_all\traffic_light\bstld_roi"

    # xml_red = r'C:\Users\chaosuix\Downloads\tl_red\xml'
    # xml_yellow = r'C:\Users\chaosuix\Downloads\tl_yellow\xml'
    # xml_green = r'C:\Users\chaosuix\Downloads\tl_green\xml'
    # xml_none = r'C:\Users\chaosuix\Downloads\tl_none\xml'

    xml_test = r'D:\xcsy\dataset\data_all\traffic_light\Tl_train_new\Annotations_2' #  xml输入

    # xml_paths = [xml_red,xml_yellow,xml_green,xml_none]
    xml_paths = [xml_test]

    # xml_paths = [xml_test_path,xml_train_path]

    print(xml_paths)

    for xml_path in xml_paths:
        # if xml_path == xml_test_path:
        #     imgs_path = r'D:\xcsy\dataset\data_all\traffic_light\Tl_bstld_test\test'
        # else:
        #     imgs_path = r'D:\xcsy\dataset\data_all\traffic_light\TL_bstld_train\images'

        xml_names = os.listdir(xml_path)
        imgs_name = os.listdir(imgs_path)

        for xml_name in xml_names:
            xml_file = os.path.join(xml_path,xml_name)
            file_name = xml_name.rsplit(".",1)[0]

            img_name = file_name + ".jpg"
            img_file = os.path.join(imgs_path,img_name)
            flag = 0
            if not os.path.isfile(img_file):
                img_name = file_name + ".png"
                img_file = os.path.join(imgs_path,img_name)
                flag = 1

            print(img_file)
            img = cv2.imread(img_file)
            # cv2.imshow("X",img)
            # cv2.waitKey()
            objs = xml_get_object(xml_file)
            rect_n = 0
            for obj in objs:
                cls = obj.findall("name")[0].text

                if cls in ['Red', 'RedLeft', 'RedRight']:
                    cls = 'tl_red'
                elif cls in ['Yellow']:
                    cls = 'tl_yellow'
                elif cls in ['off']:
                    cls = 'tl_none'
                elif cls in ['Green', 'GreenLeft', 'GreenRight']:
                    cls = 'tl_green'


                if cls in ['tl_green','tl_red','tl_yellow','tl_none']:
                    if cls=='tl_green':
                        g_nums += 1
                        roi_img_path = os.path.join(img_out_path,'tl_green')
                        mkdir(roi_img_path)
                    if cls=='tl_red':
                        r_nums += 1
                        roi_img_path = os.path.join(img_out_path, 'tl_red')
                        mkdir(roi_img_path)
                    if cls=='tl_yellow':
                        y_nums += 1
                        roi_img_path = os.path.join(img_out_path, 'tl_yellow')
                        mkdir(roi_img_path)
                    if cls=='tl_none':
                        n_nums += 1
                        roi_img_path = os.path.join(img_out_path, 'tl_none')
                        mkdir(roi_img_path)

                    rect = xml_get_rect(obj)

                    if len(rect) != 0:
                        roi_img = extract_ROI(img,rect)
                    else:
                        continue
                    roi_img_file = os.path.join(roi_img_path, file_name+"_"+str(rect_n)+".jpg")
                    rect_n += 1
                    # cv2.imshow("X",roi_img)
                    # cv2.waitKey()
                    print(roi_img_file)
                    cv2.imwrite(roi_img_file,roi_img)

    print('g_nums', g_nums)
    print('y_nums', y_nums)
    print('r_nums', r_nums)
    print('n_nums', n_nums)

