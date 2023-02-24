# -*- coding:utf-8 -*-
import openpyxl
import os

root_path = os.path.dirname(__file__)
name = os.path.join(root_path, 'test.xlsx')

wb = openpyxl.Workbook()
# wb.save('test.xlsx')

wb1 = openpyxl.load_workbook(name)
ws = wb.active


