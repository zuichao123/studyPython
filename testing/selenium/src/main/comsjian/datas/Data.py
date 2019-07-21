# coding:utf-8
'''
读写CSV文件
'''
import csv
import os


class Data(object):
    def __init__(self, path):
        self.path = path
        self.coding = 'utf-8'

    # --------------------read
    def openForRead(self):
        with open(self.path, encoding=self.coding) as f:
            reader = csv.reader(f)
            self.result = list(reader)

    def readContentsByRowNumColNum(self, rowNum, colNum):
        '''读取指定行号、列号的内容'''
        self.openForRead()
        return self.result[rowNum][colNum]

    def readContentsByRowNumColName(self, rowNum, colName):
        '''读取指定行号、列名的内容'''
        self.openForRead()
        colNum = 0
        for i in range(len(self.result[0])):
            if self.result[0][i] == colName:
                colNum = i
                break
        return self.result[rowNum][colNum]

    def readAllContents(self):
        '''读取CSV文件的所有内容'''
        self.openForRead()
        self.csvColNames = self.result[0] # 列名
        self.csvContents = self.result[1:] # 列内容

        csvContents = ''
        for i in range(len(self.csvColNames)):
            csvContents += self.csvColNames[i] + ','
        csvContents += '\n'
        for j in range(len(self.csvContents)): # 变量所有的行
            for k in range(len(self.csvContents[j])): # 变量每一行
                csvContents += self.csvContents[j][k] + ','
                if k == len(self.csvColNames)-1:
                    csvContents += '\n'
        print('readed is ok...')
        return csvContents

    # ---------------------------write

    def writeCsvContents(self, datas):
        '''写入CSV文件'''
        with open(self.path, mode='w+', newline='', encoding=self.coding) as f:
            writer = csv.writer(f)
            for row in datas:
                writer.writerow(row)
            print('writed is ok...')


if __name__ == '__main__':
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")) + "\\test\\tools\\xxx.csv"
    datas = [
        ['编号', '姓名', '年龄'],
        ['1', '小明', '13'],
        ['2', '小红', '10'],
        ['3', '小青', '15'],
    ]
    data = Data(path)

    data.writeCsvContents(datas)
    # print(data.readContentsByRowNumColName(2,'姓名'))
    # print(data.readContentsByRowNumColNum(1,2))
    print(data.readAllContents())
