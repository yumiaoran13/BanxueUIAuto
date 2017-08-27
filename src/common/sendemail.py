import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
import configread


def send_email(file):
    """
    发送邮件
    :param file: 文件路径
    :return:
    """
    with open(file, 'rb') as fp:
        mail_body = fp.read()

    send_from = 'yumiaoran13@126.com'
    send_to = ['371400140@qq.com', 'yumiaoran13@126.com']
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['subject'] = Header('自动化测试报告', 'utf-8')
    # 必须有from，否则会报554被识别为垃圾邮件无法发送
    msg['From'] = 'yumiaoran13@126.com'
    msg['To'] = ';'.join(send_to)
    smtp = smtplib.SMTP()
    smtp.connect('smtp.126.com')
    smtp.login('yumiaoran13@126.com', '1Q2w3e4r')

    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()
    print('邮件发送成功')


def get_report(report):
    """
    查找测试报告目录，找到最新测试报告文件
    :param report:
    :return:
    """
    l = os.listdir(report)
    l.sort(key=lambda fn: os.path.getmtime(report + '\\' + fn))
    report_new = os.path.join(report, l[-1])
    print(report_new)
    return report_new

if __name__ == '__main__':
    report_path = get_report(configread.prjdir + '\\report')
    send_email(report_path)
