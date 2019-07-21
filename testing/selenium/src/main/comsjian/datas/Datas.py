# coding:utf-8
"""
    使用Excel存取测试数据
    https://www.cnblogs.com/fuqia/p/8989712.html

    os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 这个是获取当前文件的上一级目录

    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 这个是把路径添加到系统的环境变量

    os.path.abspath(os.path.join(os.path.dirname(__file__),"..")) #获取当前文件的路径
"""
import os
import xlwt
import xlrd

class Datas(object):
    def __init__(self, path, sheetName):
        self.path = path
        self.sheetName = sheetName

    def getContentsBySheetname(self):
        '''读取指定sheet的属性'''
        data_sheet = xlrd.open_workbook(self.path).sheet_by_name(self.sheetName)
        # print(data_sheet.name)
        self.rows = data_sheet.nrows # 所有的行数
        self.cols = data_sheet.ncols # 所有的列数
        self.colNames = data_sheet.row_values(0) # 所有的列名
        return data_sheet

    def getValueByRownumColnum(self, rowNum, colNum):
        '''获取指定行号、指定列号的值'''
        data_sheet = self.getContentsBySheetname()
        print('---'+data_sheet.name+' opened ...')

        # 根据指定的行号、列号获取内容
        value = data_sheet.cell(rowNum, colNum)
        print(value)
        return value

    def getValueByRownumColname(self, rowNum, colName):
        '''获取指定行号、指定列名的值'''
        self.getContentsBySheetname()
        colNames = self.colNames
        i = 0
        for colNum in range(0, len(colNames)):
            if colNames[colNum] == colName:
                # print(str(i))
                data.getValueByRownumColnum(rowNum, colNum)
            i += 1

    def getAllValues(self):
        values = ''
        data_sheet = self.getContentsBySheetname()
        rows = self.rows
        cols = self.cols
        for i in range(0, rows):
            for j in range(0, cols):
                value = data_sheet.cell(i, j)
                value = str(value).split(":")[-1].replace('\'', '') + ','
                values += value
                # print(value, end="")
            values += "\n"
            # print('\n')
        return values

    # -------------------------------write--------------------------

    def set_style(self, name, height, bold=False):
        '''设置字体样式'''
        style = xlwt.XFStyle()  # 初始化样式
        font = xlwt.Font()  # 为样式创建字体
        font.name = name
        font.bold = bold
        font.color_index = 4
        font.height = height
        style.font = font
        return style

    def writeExcelContents(self, datas):
        '''写入Excel内容'''
        workbook = xlwt.Workbook(encoding='utf-8') # 创建工作簿
        self.write_data_sheet = workbook.add_sheet(self.sheetName) # 创建sheet
        # 写入所有行内容
        for j in range(len(datas)):
            for i in range(len(datas[j])):
                self.write_data_sheet.write(j, i, datas[j][i], self.set_style('Times New Roman', 220, True))
        # 保存文件
        workbook.save(self.path)

if __name__ == '__main__':
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")) + "\\test\\tools\\xxx.xlsx"
    sheetName = 'test2'
    datas = [
        ['名称', '时间', '年龄', '性别'],
        ['测试', '15:50:33-15:52:14', 32, '男'],
        ['测试3', '15:50:33-15:52:15', 33, '男'],
        ['测试2', '15:50:33-15:52:16', 34, '女']
    ]

    data = Datas(path, sheetName)
    # ------write
    data.writeExcelContents(datas)

    # ------read
    # data.getValueByRownumColnum(1, 1) # 第2行，第一列
    # data.getValueByRownumColname(1, '年龄') #第2行
    print(data.getAllValues())




