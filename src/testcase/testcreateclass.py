import unittest
from basecase import MyTest
import createclassPage
import time


class TestCreateClass(MyTest):
    """创建班级"""
    def test_create_class(self):
        """创建机构班级"""
        createclass = createclassPage.CreateClass(self.driver)
        createclass.click_school()
        createclass.search('机构')
        createclass.set_school()
        createclass.set_grade()
        now = time.strftime('%m%d%H%M')
        createclass.set_classname(now)
        createclass.set_subject(2)
        createclass.click_create()
        createclass.click_ok()
        self.assertEqual(createclass.get_activity(), '.main.CreateClassSuccessActivity', '页面跳转错误，创建班级失败')

if __name__ == '__main__':
    unittest.main()
