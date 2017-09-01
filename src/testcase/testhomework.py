from basecase import MyTest
from configread import ConfigRead
import unittest
import time


class TestHomeWork(MyTest):
    """布置作业"""
    def test_home_work_tongbu(self):
        """按同步练习布置测试"""
        eleinfo = ConfigRead('控件.ini')
        ele.click(*eleinfo.get_elinfo('学堂', '布置作业'))
        ele.click(*eleinfo.get_elinfo('布置作业', '选择学科'))

        # elist = ele.find_elements(*eleinfo.get_elinfo('布置作业', '学科列表'))
        # index = random.randint(0, len(elist) - 1)
        ele.clicks(*eleinfo.get_elinfo('布置作业', '学科列表'), index=1)
        ele.click(*eleinfo.get_elinfo('布置作业', '选择班级'))
        ele.clicks(*eleinfo.get_elinfo('布置作业', '班级列表'), index=0)
        ele.clicks(*eleinfo.get_elinfo('布置作业', '年级列表'), index=0)
        ele.click(*eleinfo.get_elinfo('布置作业', '确定班级'))
        ele.click(*eleinfo.get_elinfo('布置作业', '选择教材'))
        ele.clicks(*eleinfo.get_elinfo('布置作业', '版本列表'), index=0)
        ele.clicks(*eleinfo.get_elinfo('布置作业', '版本列表'), index=3)
        ele.click(*eleinfo.get_elinfo('布置作业', '选择内容'))
        time.sleep(10)
        ele.click(*eleinfo.get_elinfo('布置作业', '选择内容'))
        ele.clicks(*eleinfo.get_elinfo('布置作业', '添加题目'), index=0)
        ele.click(*eleinfo.get_elinfo('布置作业', '布置作业'))
        ele.click(*eleinfo.get_elinfo('布置作业', '确认布置'))

if __name__ == '__main__':
    unittest.main()
