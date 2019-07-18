# coding:utf-8
"""
    使用CSV存储测试数据
"""
import xlrd

class Datas(object):
    def __init__(self, path):
        self.path = path

    def open_excel(self):
        '''打开Excel'''
        work = xlrd.open_workbook(self.path)
        print('---excel open ...')
        return work

    def getSheetByIndex(self, index):
        '''根据索引读取'''
        # data_sheet = self.open_excel().sheets()[index]
        data_sheet = self.open_excel().sheet_by_index(index)
        print(data_sheet.name)
        return data_sheet

    def getValueForRowAndCol(self, sheetName, rowNum, colNum):
        '''获取指定sheet、指定行、指定列的值'''
        data_sheet = self.open_excel().sheet_by_name(sheetName)
        print('---'+data_sheet.name+' opened ...')

        # 根据指定的行号、列号获取内容
        value = data_sheet.cell(rowNum, colNum)
        print(value)
        return value

    def getColNames(self, sheetName):
        '''获取指定sheet的所有列名'''
        data_sheet = self.open_excel().sheet_by_name(sheetName)
        colNames = data_sheet.row_values(0)
        print(colNames)
        return colNames

if __name__ == '__main__':
    path = "C:/Software/pycharm/workspace/studyPython/testing/selenium/src/test/tools/xxx.xlsx"

    data = Datas(path)
    data.open_excel()
    print('--------------')
    # data.getSheetByIndex(3)
    # print('--------------')
    colNames = data.getColNames(u'Sheet4')
    i = 0
    for name in range(0, len(colNames)):
        if colNames[name] == '年龄':
            print(str(i))
            data.getValueForRowAndCol(u'Sheet4', i, i)
        i += 1
    print('--------------')
