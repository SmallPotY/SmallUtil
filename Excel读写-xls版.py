# -*- coding:utf-8 -*-
import xlwt
import xlrd

def writeExcel(content,name):
    # 写excel
    workbook = xlwt.Workbook(encoding='utf-8')  # 创建工作簿对象
    sheet = workbook.add_sheet(name)  # 新建sheet

    # 遍历内容写入
    for r_index, row in enumerate(content):
        for c_index,column in enumerate(row):
            sheet.write(r_index, c_index, content[r_index][c_index])  

    fileName = name + '.xls'
    workbook.save(fileName)  # 保存


def readExcel(file):
    # 读Excel
    wb = xlrd.open_workbook(filename=file)

    sheet_names = wb.sheet_names() # 获取所有表格名字
    sheet1 = wb.sheet_by_index(0)   # 通过索引获取表格
    sheet2 = wb.sheet_by_name('test')   # 通过名字获取表格

    sheetName = sheet1.name     # 工作表名
    sheetRows = sheet1.nrows    # 总行数
    sheetCols = sheet1.ncols    # 总列数

    for x in range(sheetRows):
        for y in range(sheetCols):
            print( sheet1.cell(x,y).value )  # 读取单元格方法一
            print( sheet1.cell_value(x,y) )  # 读取单元格方法二
            print( sheet1.row(x)[y].value )  # 读取单元格方法三




# content = [["序号","编号","数量"],[1,"test001",4],[2,"test002",3],[3,"test003",4],[4,"test004",3]]
# writeExcel(content,"test")
readExcel("test.xls")