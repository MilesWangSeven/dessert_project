import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 创建SMTP_SSL对象
qq_mail = smtplib.SMTP_SSL('smtp.qq.com', 465)
# 指定用户邮箱
user_mail = input('请输入QQ邮箱:')
# 输入邮箱密码
password_mail = input('请输入登陆码:')
# 登陆邮箱
qq_mail.login(user_mail, password_mail)

# 收件邮箱列表
recipient_list = ['wufeng@qq.com', 'forchange@qq.com']
mail_msg = '''
吴枫老师：
    你好，我爱Python。
            你的学生 Miles Wang
'''
# 创建邮箱对象
message = MIMEText(mail_msg, 'plain', 'utf-8')
# 对象类似字典型赋值
message['Subject'] = Header('我爱Python', 'utf-8')
message['From'] = Header('Miles Wang', 'utf-8')
message['To'] = Header('吴枫老师', 'utf-8')
try:
    # 按照发送邮箱,接收邮箱内容,内容来发送
    qq_mail.sendmail(user_mail, recipient_list, message.as_string())
    print('已发送成功')
except smtplib.SMTPException as e:
    print('Error:{}'.format(e))
# 退出登陆
qq_mail.quit()
