# coding:utf-8
"""
    发送邮件类
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SendEmail(object):
    def __init__(self, senderFrom, passwd):
        self.senderFrom = senderFrom  # 发件人邮箱
        self.passwd = passwd  # 发件人邮箱授权码或密码

    def set_constans(self, subject):
        '''设置主题'''
        self.subject = subject
        return self.subject

    def set_projectName(self, projectName):
        '''设置项目名称'''
        self.projectName = projectName
        return self.projectName

    def set_mainBody(self, mainBody):
        '''设置正文'''
        self.mainBody = mainBody
        return self.mainBody

    def set_fuJian(self, fjs_path):
        '''添加附件'''
        self.fjs = fjs_path
        return self.fjs

    def sender(self, senderTo):
        '''发送'''
        # 创建一个带附件的实例
        msg = MIMEMultipart()
        msg['Subject'] = self.subject
        print(self.subject)
        msg['From'] = self.senderFrom
        msg['To'] = senderTo

        # 创建正文，将文本文件添加到MIMEMultipart中
        msg.attach(MIMEText(self.mainBody, 'html', 'utf-8'))

        if(len(self.fjs) > 0): # 如果有附件
            print('附件的大小为：'+str(len(self.fjs)))
            for i in range(0, len(self.fjs)): # 构造附件
                fj_path = str(self.fjs[i])
                print('--------------->>>'+fj_path)
                # 构造附件1，传送当前目录下文件
                i = MIMEText(open(fj_path , 'rb').read(),'base64','utf-8') # rb以二进制方式读取
                # filename为附件名称，可以任意写，写什么名字，邮件中显示什么名字
                filename = fj_path.split('\\')[-1]
                print('-------------->'+filename)
                i["Content-Disposition"] = "attachment; filename = " + filename
                # 将附件添加到MIMEMultipart中
                msg.attach(i)

        try:
            s = smtplib.SMTP('smtp.irisking.com',25)
            s.set_debuglevel(0) # 输出发送邮件详细过程(1输出 0不输出)
            s.login(self.senderFrom, self.passwd)
            s.sendmail(self.senderFrom,senderTo,msg.as_string())
            print('Send Succese')
        except:
            print('Send Failure')

if __name__ == "__main__":
        senderFrom = 'sunjian@irisking.com' # 发件人邮箱
        passwd = 'cronaldo7' # 发件人邮箱授权码或密码
        projectName = 'xxx system' # 项目名称
        subject = projectName + ' 测试报告' # 主题
        senderTo = 'sunjian@irisking.com' # 收件人邮箱
        mainbody = '<font color=\"red\">(本邮件是程序自动下发的，请勿回复！)</font><br>各位领导同事，大家好：<br>&nbsp;&nbsp;&nbsp;&nbsp;' + projectName + ' 测试已完成，测试详情请查看附件测试报告，谢谢。<br><br><br>————————————————————<br>孙健<br>软件测试工程师<br>电话：15510211823<br>Email：' + senderFrom  # 正文
        fjs_path = ['C:\\a.txt', 'C:\\b.html'] # 附件地址

        send = SendEmail(senderFrom, passwd)
        send.set_projectName(projectName)
        send.set_constans(subject)
        send.set_mainBody(mainbody)
        send.set_fuJian(fjs_path)

        send.sender(senderTo)
