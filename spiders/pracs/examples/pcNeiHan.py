# coding:gbk
"""
    ��ȡ�ں�����
"""
from urllib import request,parse
import urllib
import re

class Spider:
    def __init__(self):
        # ��ʼ����ʼҳλ��
        self.page = 4025518
        # ��ȡ���أ����ΪTrue������ȡ
        self.switch = True

    def loadPage(self):
        """
            ���ã�����ҳ��
        """
        print ("������������....")
        url = "http://www.xuexila.com/duanzi/nahanduanzi/" + str(self.page) + ".html"
        headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
        request = urllib.request.Request(url, headers = headers)
        response = urllib.request.urlopen(request)

        # ��ȡÿҳ��HTMLԴ���ַ���
        html = response.read()

        # ����������ʽ�������ƥ��ÿҳ��Ķ������ݣ�re.S ��ʾƥ��ȫ���ַ�������
        pattern = re.compile('<p>(.*?)</p>', re.S)

        # ������ƥ�����Ӧ�õ�htmlԴ���ַ�����������ҳ��������ж��ӵ��б�
        content_list = pattern.findall(str(html))

        # ����dealPage() ���������������Ӱ�
        self.dealPage(content_list)

    def dealPage(self, content_list):
        """
            ����ÿҳ�Ķ���
            content_list : ÿҳ�Ķ����б���
        """
        for item in content_list:
            # ���������ÿ�����Ӱ��������滻����������
            item = item.replace("<p>","").replace("</p>", "")
            # ����������writePage() ��ÿ������д���ļ���
            # self.writePage(item)

    def writePage(self, item):
        """
            ��ÿ���������д���ļ���
            item: ������ÿ������
        """
        # д���ļ���
        print ("����д������....")
        with open("duanzi.txt", "w+") as f:
            f.write(item.encode("latin1").decode("gbk"))

    def startWork(self):
        """
            ������������
        """
        # ѭ��ִ�У�ֱ�� self.switch == False
        while self.switch:
            # �û�ȷ����ȡ�Ĵ���
            self.loadPage()
            command = input("���������ȡ���밴�س����˳�����quit)")
            if command == "quit":
                # ���ֹͣ��ȡ�������� quit
                self.switch = False
            # ÿ��ѭ����pageҳ������1
            self.page += 1
        print ("ллʹ�ã�")


if __name__ == "__main__":
    duanziSpider = Spider()
#    duanziSpider.loadPage()
    duanziSpider.startWork()