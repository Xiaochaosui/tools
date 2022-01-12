import os
import xml.etree.ElementTree as ET
import shutil
from pathlib import Path
def mkdir(path):
    if not os.path.isdir(path):
        os.makedirs(path)

# extend = ['tl_green','tl_red','tl_yellow','tl_none','Green', 'GreenLeft', 'GreenRight','off','Red', 'RedLeft', 'RedRight','Yellow']
# extend = ['rider']


def get_sourceTxt(infer_path):
    path = Path(infer_path)
    dirs = os.listdir(path)
    res = []
    for dir in dirs:
        source_txt = path / Path(dir) / "source.txt"
        with open(source_txt, "r", encoding="utf-8") as f:
            path_source = f.readline().replace("\n", "")
        # print(path_list)
        res.append(path_source)
    return res

def copy_rawimg_from_extend(xml_input_path,image_input_path,root_output,extend):
    image_output_path = os.path.join(root_output, 'JPEGImages')
    xml_output_path = os.path.join(root_output, 'Annotations')
    # print(xml_output_path)
    mkdir(image_output_path)
    mkdir(xml_output_path)
    n = 0
    for image_input in os.listdir(image_input_path):
        img_formate = Path(image_input).suffix
        # print("img_formate:",img_formate)
        xml_input = image_input.replace(img_formate,".xml")
        # print("xml_input:",xml_input)
        # break
        print(os.path.join(xml_input_path, xml_input))
        tree = ET.parse(os.path.join(xml_input_path, xml_input))
        root = tree.getroot()
        for object in root.findall("object"):
            name = object.findall("name")[0].text
            print(name)
            # if name in extend and not os.path.isfile(os.path.join(xml_output_path, xml_input)):
            if name and not os.path.isfile(os.path.join(xml_output_path, xml_input)):
                n += 1
                print("$$$")
                shutil.copy(os.path.join(xml_input_path, xml_input), os.path.join(xml_output_path, xml_input))
                shutil.copy(os.path.join(image_input_path, image_input), os.path.join(image_output_path, image_input))
                print('{} 已完成{}'.format(n, xml_input))
                break

if __name__ == '__main__':

    # extend = ['tl_green','tl_red','tl_yellow','tl_none','person','arrows_right','arrows_left','arrows_straight','arrows_straight_right','arrows_straight_left','arrows_turn','rider','Lingxing','rectangle','triangle','liubianxing','circle']
    extend = ['rider']
    # root_input = r'D:\xcsy\245_246\detect\mutil-model-test\All_Results'  # 输入根目录
    root_output = r'D:\xcsy\245_246\detect\rider_detect\rider_infer_1_out'  # 输出根目录


    # root = Path(r"D:\xcsy\245_246\detect\rider_检测\rider_infer")
    root_input = r"D:\xcsy\245_246\detect\rider_detect\rider_infer_1"
    # image_input_path = os.path.join(root_input, 'JPEGImages')  # 被复制的图片
    image_input_path= r"D:\xcsy\245_246\detect\rider_detect\rider_infer_1\JPEGImages"
    xml_input_path = os.path.join(root_input, 'Annotations') # 根据的xml信息
    # for dir in os.listdir(str(root)):
    #     source_txt = root / Path(dir) / "source.txt"
    #     with open(source_txt, "r", encoding="utf-8") as f:
    #         image_input_path = f.readline().replace("\n", "")
    #     xml_input_path =  root / Path(dir) / "All_Results/All_Annotations"
    #     print("image_input_path:",image_input_path)
    #     print("xml_input_path:",str(xml_input_path))

    copy_rawimg_from_extend(str(xml_input_path), image_input_path, root_output,extend)
        # break





