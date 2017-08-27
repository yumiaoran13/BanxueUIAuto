# 用例执行总入口
import unittest
import HTMLTestReportCN
# import HTMLTestRunner
import time
import sendemail
import configread

discover = unittest.defaultTestLoader.discover(configread.prjdir, pattern='test*.py')

now = time.strftime('%Y-%m-%d %H-%M-%S')
report_path = configread.prjdir + '\\report\\' + now + 'UIAutoReport.html'
with open(report_path, 'wb') as fp:
    runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                             title=u'自动化测试报告',
                                             description=u'环境：夜神安卓模拟器4.4.2',
                                             tester=u"于淼然",
                                             )
    runner.run(discover)
report_path = sendemail.get_report(configread.prjdir + '\\report')
sendemail.send_email(report_path)
