# -*- coding: utf-8 -*- 
# @Time    : 2022/1/10 14:55
# @Author  : xiaochaosui
# @File    : 14_txt2excel.py
# @Software: PyCharm
# @Email   : chaosuixiao@gmail.com
'''

读取txt到excel中去

labels images P R  mAP@.5  mAP@.5:.95
'''
import openpyxl
def read_txt(file):
    with open(file) as f:
        data = f.readlines()
        res = []
        for line in data:
            temple = []
            data_line = [x for x in line.split(" ") if x!='']
            data_line.remove(data_line[2])
            # print(data_line)
            res.append(data_line)
            # for x in data_line[1:]: #cx,cy,rw,rh
            #     temple.append(float(x))
    return res

def write_excel(file,data):
    workbook = openpyxl.load_workbook(file)
    worksheet = workbook.get_sheet_by_name('Sheet3')
    for row_index, row_item in enumerate(data):
        for col_index, col_item in enumerate(row_item):
            # 写入
            print(col_item)
            if '\n' in col_item:
                col_item = col_item.replace("\n",'')
            worksheet.cell(row=row_index + 1, column=col_index + 1, value=col_item)

    # worksheet.write(0,0,"111")
    # print(row3)
    workbook.save('excelwrite1.xlsx')


if __name__ == '__main__':
    txt_file = r"C:\Users\chaosuix\Desktop\best.txt"
    excel_file = r"C:\Users\chaosuix\Desktop\模型指标 - update.xlsx"
    data_txt = read_txt(txt_file)
    write_excel(excel_file,data_txt)
    # print(data_txt)