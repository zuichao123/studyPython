# coding:utf-8
"""
发送邮件
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


senduser = 'xxxx@139.com'    #发件人邮箱
passwd = 'xxxxxxxx'                 #发件人邮箱授权码或密码
receivers = 'xxxxxxx@139.com'       #收件人邮箱
subject = '运维报告'    #主题

# 创建一个带附件的实例
msg = MIMEMultipart()
msg['Subject'] = subject
msg['From'] = senduser
msg['To'] = receivers

#创建正文，将文本文件添加到MIMEMultipart中
msg.attach(MIMEText('您好：xxx系统的测试报告，请查收','plain','utf-8'))

#构造附件1，传送当前目录下文件
att1 = MIMEText(open(r'c:\sum.txt','rb').read(),'base64','utf-8') # rb以二进制方式读取
# filename为附件名称，可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = "attachment; filename = sum.txt"
#将附件添加到MIMEMultipart中
msg.attach(att1)

#构造附件2
att2 = MIMEText(open(r'c:\sum.csv','rb').read(),'base64','utf-8')
att2["Content-Disposition"] = "attachment; filename =sum.csv"
#将附件添加到MIMEMultipart中
msg.attach(att2)

try:
    s = smtplib.SMTP('mail.139.com',25)
    s.set_debuglevel(1) #输出发送邮件详细过程
    s.login(senduser,passwd)
    s.sendmail(senduser,receivers,msg.as_string())
    print('Send Succese')
except:
    print('Send Failure')
