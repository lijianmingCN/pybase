# -*- coding: UTF-8 -*-
'''
发送邮件主要用到了smtplib和email两个模块，这里首先就两个模块进行一下简单的介绍：
1、smtplib模块
smtplib.SMTP([host[, port[, local_hostname[, timeout]]]])
SMTP类构造函数，表示与SMTP服务器之间的连接，通过这个连接可以向smtp服务器发送指令，执行相关操作（如：登陆、发送邮件）。所有参数都是可选的。
host：smtp服务器主机名
port：smtp服务的端口，默认是25；如果在创建SMTP对象的时候提供了这两个参数，在初始化的时候会自动调用connect方法去连接服务器。
smtplib模块还提供了SMTP_SSL类和LMTP类，对它们的操作与SMTP基本一致。
smtplib.SMTP提供的方法：
SMTP.set_debuglevel(level)：设置是否为调试模式。默认为False，即非调试模式，表示不输出任何调试信息。
SMTP.connect([host[, port]])：连接到指定的smtp服务器。参数分别表示smpt主机和端口。注意: 也可以在host参数中指定端口号（如：smpt.yeah.net:25），这样就没必要给出port参数。
SMTP.docmd(cmd[, argstring])：向smtp服务器发送指令。可选参数argstring表示指令的参数。
SMTP.helo([hostname]) ：使用"helo"指令向服务器确认身份。相当于告诉smtp服务器“我是谁”。
SMTP.has_extn(name)：判断指定名称在服务器邮件列表中是否存在。出于安全考虑，smtp服务器往往屏蔽了该指令。
SMTP.verify(address) ：判断指定邮件地址是否在服务器中存在。出于安全考虑，smtp服务器往往屏蔽了该指令。
SMTP.login(user, password) ：登陆到smtp服务器。现在几乎所有的smtp服务器，都必须在验证用户信息合法之后才允许发送邮件。
SMTP.sendmail(from_addr, to_addrs, msg[, mail_options, rcpt_options]) ：发送邮件。这里要注意一下第三个参数，msg是字符串，表示邮件。我们知道邮件一般由标题，发信人，收件人，邮件内容，附件等构成，发送邮件的时候，要注意msg的格式。这个格式就是smtp协议中定义的格式。
SMTP.quit() ：断开与smtp服务器的连接，相当于发送"quit"指令。（很多程序中都用到了smtp.close()，具体与quit的区别google了一下，也没找到答案。）
2、email模块
emial模块用来处理邮件消息，包括MIME和其他基于RFC 2822 的消息文档。使用这些模块来定义邮件的内容，是非常简单的。其包括的类有（更加详细的介绍可见：http://docs.python.org/library/email.mime.html）：
class email.mime.base.MIMEBase(_maintype, _subtype, **_params)：这是MIME的一个基类。一般不需要在使用时创建实例。其中_maintype是内容类型，如text或者image。_subtype是内容的minor type 类型，如plain或者gif。 **_params是一个字典，直接传递给Message.add_header()。
class email.mime.multipart.MIMEMultipart([_subtype[, boundary[, _subparts[, _params]]]]：MIMEBase的一个子类，多个MIME对象的集合，_subtype默认值为mixed。boundary是MIMEMultipart的边界，默认边界是可数的。
class email.mime.application.MIMEApplication(_data[, _subtype[, _encoder[, **_params]]])：MIMEMultipart的一个子类。
class email.mime.audio. MIMEAudio(_audiodata[, _subtype[, _encoder[, **_params]]])： MIME音频对象
class email.mime.image.MIMEImage(_imagedata[, _subtype[, _encoder[, **_params]]])：MIME二进制文件对象。
class email.mime.message.MIMEMessage(_msg[, _subtype])：具体的一个message实例，使用方法如下：
msg=mail.Message.Message()    #一个实例 
msg['to']='XXX@XXX.com'      #发送到哪里 
msg['from']='YYY@YYYY.com'       #自己的邮件地址 
msg['date']='2012-3-16'           #时间日期 
msg['subject']='hello world'    #邮件主题 
class email.mime.text.MIMEText(_text[, _subtype[, _charset]])：MIME文本对象，其中_text是邮件内容，_subtype邮件类型，可以是text/plain（普通文本邮件），html/plain(html邮件),  _charset编码，可以是gb2312等等。

注：MIME 参考手册：http://www.w3school.com.cn/media/media_mimeref.asp
'''
import smtplib
import mimetypes
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
mailto_list=['234012921@qq.com']
mail_host="smtp.163.com"  #设置服务器
mail_user="18515153565@163.com"    #用户名
mail_pass="qq4821032706"   #口令
mail_postfix="163.com"  #发件箱的后缀
#普通文本邮件
#普通文本邮件发送的实现，关键是要将MIMEText中_subtype设置为plain。
#首先导入smtplib和mimetext。创建smtplib.smtp实例，connect邮件smtp服务器，login后发送
def send_mail(to_list,sub,content):  
    me="Niklaus"+"<"+mail_user+">"  
    msg = MIMEText(content,_subtype='plain',_charset='gb2312')  
    msg['Subject'] = sub  
    msg['From'] = me  
    msg['To'] = ";".join(to_list)  
    try:  
        server = smtplib.SMTP()  
        server.connect(mail_host)  
        server.login(mail_user,mail_pass)  
        server.sendmail(me, to_list, msg.as_string())  
        server.close()  
        return True  
    except Exception, e:  
        print str(e)  
        return False
    
#html邮件的发送
#与text邮件不同之处就是将将MIMEText中_subtype设置为html。
def send_mail2(to_list,sub,content):  #to_list：收件人；sub：主题；content：邮件内容
    me="Niklaus"+"<"+mail_user+"@"+mail_postfix+">"   #这里的hello可以任意设置，收到信后，将按照设置显示
    msg = MIMEText(content,_subtype='html',_charset='utf-8')    #创建一个实例，这里设置为html格式邮件
    msg['Subject'] = sub    #设置主题
    msg['From'] = me  
    msg['To'] = ";".join(to_list)  
    try:  
        s = smtplib.SMTP()  
        s.connect(mail_host)  #连接smtp服务器
        s.login(mail_user,mail_pass)  #登陆服务器
        s.sendmail(me, to_list, msg.as_string())  #发送邮件
        s.close()  
        return True  
    except Exception, e:  
        print str(e)  
        return False  

#发送带附件的邮件
#发送带附件的邮件，首先要创建MIMEMultipart()实例，然后构造附件，如果有多个附件，可依次构造，最后利用smtplib.smtp发送。
def send_mail3(to_list,sub,content):
    msg = MIMEMultipart()#创建一个带附件的实例
    #构造附件1
    att1 = MIMEText(open('d:\\123.rar', 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="123.rar"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
    msg.attach(att1)
    #构造附件2
    att2 = MIMEText(open('d:\\123.txt', 'rb').read(), 'base64', 'utf-8')
    att2["Content-Type"] = 'application/octet-stream'
    att2["Content-Disposition"] = 'attachment; filename="123.txt"'
    msg.attach(att2)
    #加邮件头
    me="Niklaus"+"<"+mail_user+"@"+mail_postfix+">"
    msg['Subject'] = sub    #设置主题
    msg['From'] = me  
    msg['To'] = ";".join(to_list)
    #发送邮件
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user,mail_pass)#XXX为用户名，XXXXX为密码
        server.sendmail(me, to_list, msg.as_string())
        server.quit()
        return True
    except Exception, e:  
        print str(e)
        return False
    
#利用MIMEimage发送图片    
def AutoSendMail(to_list,sub,content):
    msg = MIMEMultipart()
    me="Niklaus"+"<"+mail_user+"@"+mail_postfix+">"
    msg['Subject'] = sub    #设置主题
    msg['From'] = me  
    msg['To'] = ";".join(to_list)
    txt = MIMEText("这是中文的邮件内容哦",'plain','utf-8')     
    msg.attach(txt)
    file = "D:\\1.png"
    image = MIMEImage(open(file,'rb').read())
    image.add_header('Content-ID','<image1>')
    image["Content-Type"] = "image/jpeg"
    image["Content-Disposition"] = 'attachment; filename="123.jpeg"'
    msg.attach(image)
    server = smtplib.SMTP()
    server.connect(mail_host)
    server.login(mail_user,mail_pass)
    server.sendmail(me, to_list, msg.as_string())
    server.quit()
    
     
if __name__ == '__main__':  
    if send_mail(mailto_list,"hello","hello world"):  
        print "发送成功"  
    else:
        print "发送失败"  
    
    #if send_mail2(mailto_list,"hello","<a href='http://www.cnblogs.com/xiaowuyi'>小五义</a>"):
    #    print "发送成功"
    #else:
    #    print "发送失败"

    #if send_mail3(mailto_list,"hello","hello world"):
    #    print "发送成功"
    #else:
    #    print "发送失败"
    
    #AutoSendMail(mailto_list,"hello","hello world")
    
    