# @Author:xiaochaosui
# @Organization:FiberHome
# @Email:chaosuixiao@gmail.com
# @Time:2021/12/2 15:30
import os
import  shutil
import  xml.etree.cElementTree as xml_tree
def add_xml(paths,save_path):
    print("="*5 +" Merge XML " + "="*5)
    if os.path.exists(save_path):
        shutil.rmtree(save_path)
    # print("Root_path:",paths[0])
    shutil.copytree(paths[0],save_path)
    files = os.listdir(paths[0])
    # print(files)
    for anna_file in files:
        res_xml = os.path.join(save_path, anna_file)
        if os.path.exists(res_xml):
            ID = 0
            res_tree = xml_tree.parse(res_xml)
            res_root = res_tree.getroot()
            res_objects = res_root.findall('object')
            for res_obj in res_objects:
                ID = int(res_obj.findall("ID")[0].text)
                # print(res_obj.findall("ID")[0].text)
            for path in paths[1:]:
                print(res_xml + " merge ", path + '/' + anna_file)
                tree = xml_tree.parse(path + '/' + anna_file)
                root = tree.getroot()
                objects = root.findall('object')
                for obj in objects:
                    ID += 1
                    obj.findall("ID")[0].text = str(ID)
                    res_root.append(obj)
            res_tree.write(res_xml, encoding='utf-8')
        else:
            print(res_xml,"not exist")
        break


if __name__ == '__main__':
    paths =[
        r"D:\xcsy\245_246\test_code\Person\Annotations",
        r"D:\xcsy\245_246\test_code\Car\Annotations",
        r"D:\xcsy\245_246\test_code\Rider\Annotations"
    ]
    save_path=r"D:\xcsy\245_246\test_code\all"
    add_xml(paths,save_path)