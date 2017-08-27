from basecase import MyTest
import time
import loginPage
from configread import ConfigRead
import unittest
import random


class TestStudy(MyTest):
    """学习圈"""
    def test_create_school(self):
        """发布学习圈测试"""
        ele = loginPage.Login(self.driver)
        ele.login()
        eleinfo = ConfigRead('控件.ini')
        ele.click(*eleinfo.get_elinfo('导航', '发现'))
        ele.click(*eleinfo.get_elinfo('学习圈', '学习圈'))
        ele.click(*eleinfo.get_elinfo('学习圈', '添加'))
        now = time.strftime('%Y-%m-%d %H-%M-%S')
        value = '这是一条自动发出的学习圈' + now
        ele.send_key(*eleinfo.get_elinfo('学习圈', '内容'), value=value)
        ele.click(*eleinfo.get_elinfo('学习圈', '选择学校'))
        elist = ele.find_elements(*eleinfo.get_elinfo('学习圈', '学校列表'))
        index = random.randint(0, len(elist) - 1)
        ele.clicks(*eleinfo.get_elinfo('学习圈', '学校列表'), index=index)
        ele.click(*eleinfo.get_elinfo('学习圈', '发布'))

if __name__ == '__main__':
    unittest.main()
