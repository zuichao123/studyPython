# coding:utf-8
"""
发送邮件
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

class SendEmail(object):
    def __init__(self, senderFrom, passwd):
        self.senderFrom = senderFrom  # 发件人邮箱
        self.passwd = passwd  # 发件人邮箱授权码或密码

    def constans(self, subject):
        return subject  # 主题

    def projectName(self, projectName):
        return projectName

    def fuJian(self, arg1, arg2):
        fj = []
        fj.append(arg1)
        fj.append(arg2)
        return fj

    def sender(self, senderTo):
        # 创建一个带附件的实例
        msg = MIMEMultipart()
        msg['Subject'] = self.constans
        print(self.constans)
        msg['From'] = self.senderFrom
        msg['To'] = senderTo

        #创建正文，将文本文件添加到MIMEMultipart中
        msg.attach(MIMEText('<font color=\"red\">(本邮件是程序自动下发的，请勿回复！)</font><br>各位领导同事，大家好：<br>&nbsp;&nbsp;&nbsp;&nbsp;' + self.projectName + '测试已完成，测试详情请查看附件测试报告，谢谢。<br><br><br>————————————————————<br>孙健<br>软件测试工程师<br>电话：15510211823<br>Email：' + self.senderFrom, 'plain', 'utf-8'))

        #构造附件1，传送当前目录下文件
        att1 = MIMEText(open(r'C:\Users\sunjian\Desktop\sum.txt','rb').read(),'base64','utf-8') # rb以二进制方式读取
        # filename为附件名称，可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = "attachment; filename = sum.txt"
        #将附件添加到MIMEMultipart中
        msg.attach(att1)

        #构造附件2
        att2 = MIMEText(open(r'C:\Users\sunjian\Desktop\sum.csv','rb').read(),'base64','utf-8')
        att2["Content-Disposition"] = "attachment; filename =sum.csv"
        #将附件添加到MIMEMultipart中
        msg.attach(att2)

        try:
            print(msg.as_string())
            s = smtplib.SMTP('smtp.irisking.com',25)
            s.set_debuglevel(1) # 输出发送邮件详细过程
            s.login(self.senderFrom, self.passwd)
            s.sendmail(self.senderFrom,senderTo,msg.as_string())
            print('Send Succese')
        except:
            print('Send Failure')

if __name__ == "__main__":
        senderFrom = 'sunjian@irisking.com'  # 发件人邮箱
        passwd = 'cronaldo7'  # 发件人邮箱授权码或密码
        projectName = 'xxx system testReport'
        subject = '测试报告'  # 主题
        senderTo = 'sunjian@irisking.com'  # 收件人邮箱

        send = SendEmail(senderFrom, passwd)

        send.projectName(projectName)
        send.constans(subject)
        send.sender(senderTo)

