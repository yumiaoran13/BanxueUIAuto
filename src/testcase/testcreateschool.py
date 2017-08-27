from basecase import MyTest
import time
import loginPage
from configread import ConfigRead
import unittest
import random


class TestCreateSchool(MyTest):
    """创建学校"""
    def test_create_school(self):
        """创建学校测试"""
        ele = loginPage.Login(self.driver)
        ele.login()
        eleinfo = ConfigRead('控件.ini')
        ele.click(*eleinfo.get_elinfo('学堂', '班级管理'))
        ele.click(*eleinfo.get_elinfo('班级管理', '创建班级'))
        ele.click(*eleinfo.get_elinfo('班级管理', '选择学校'))
        ele.click(*eleinfo.get_elinfo('班级管理', '创建学校'))
        now = time.strftime('%Y%m%d%H%M%S')
        name = u'学校' + now
        ele.send_key(*eleinfo.get_elinfo('班级管理', '学校名称'), value=name)
        ele.click(*eleinfo.get_elinfo('班级管理', '所在区域'))

        while True:
            elist = ele.find_elements(*eleinfo.get_elinfo('班级管理', '选择省市'))
            index = random.randint(0, len(elist) - 1)
            ele.clicks(*eleinfo.get_elinfo('班级管理', '选择省市'), index=index)
            if self.driver.current_activity == '.school.classmanager.AddSchoolActivity':
                break

        ele.click(*eleinfo.get_elinfo('班级管理', '保存'))

    def test_create_institution(self):
        """创建机构测试"""
        ele = loginPage.Login(self.driver)
        ele.login()
        eleinfo = ConfigRead('控件.ini')
        ele.click(*eleinfo.get_elinfo('学堂', '班级管理'))
        ele.click(*eleinfo.get_elinfo('班级管理', '创建班级'))
        ele.click(*eleinfo.get_elinfo('班级管理', '选择学校'))
        ele.click(*eleinfo.get_elinfo('班级管理', '创建学校'))
        ele.click(*eleinfo.get_elinfo('班级管理', '类型机构'))
        now = time.strftime('%Y%m%d%H%M%S')
        name = u'机构' + now
        ele.send_key(*eleinfo.get_elinfo('班级管理', '学校名称'), value=name)
        ele.click(*eleinfo.get_elinfo('班级管理', '所在区域'))
        # 随机选择省市区
        while True:
            elist = ele.find_elements(*eleinfo.get_elinfo('班级管理', '选择省市'))
            index = random.randint(0, len(elist) - 1)
            ele.clicks(*eleinfo.get_elinfo('班级管理', '选择省市'), index=index)
            if self.driver.current_activity == '.school.classmanager.AddSchoolActivity':
                break

        ele.click(*eleinfo.get_elinfo('班级管理', '保存'))

if __name__ == '__main__':
    unittest.main()
