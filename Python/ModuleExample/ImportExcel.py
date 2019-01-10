#coding=utf-8
import xlrd
from xlutils.copy import copy
import os

######################
# 文件读取
######################
#读取的文件路径
file_path = r'./path/to/excel.xlsx'

# 此代码可以不用
#文件中的中文转码
file_path = file_path.decode('utf-8')


#获取数据
data = xlrd.open_workbook(file_path)

#获取sheet
table = data.sheet_by_index(0)


######################
# 读取表内信息
######################
#获取总行数
nrows = table.nrows
print("row num: ", nrows)
#获取总列数
ncols = table.ncols
print("col num: ",ncols)

#获取一行的数值
print(table.row_values(1))

# 获取一列的数值
print(table.col_values(1))
print(table.col_values(0))

#获取一个单元格的数值
cell_value = table.cell(1,1).value
print(cell_value)


######################
# Excel表格的写操作
######################
book = xlrd.open_workbook(file_path)
#复制一个excel
new_book = copy(book)#复制了一份原来的excel
#通过获取到新的excel里面的sheet页
sheet = new_book.get_sheet(0)#获取到第一个sheet页
#写入excel，第一个值是行，第二个值是列
sheet.write(6, 0, 'Dandan Sun')
#保存新的excel，保存excel必须使用后缀名是.xls的，不是能是.xlsx的
new_book.save('stu_new.xls')

#删除旧文件并重命名以做到修改文件的效果
os.remove('stu.xls')
os.rename('stu_new.xls','stu.xls')