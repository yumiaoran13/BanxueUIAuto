from basecase import MyTest
import createschoolPage
import unittest
import random


class TestCreateSchool(MyTest):
    """创建学校"""
    def test_create_school(self):
        """创建学校"""
        crreateschool = createschoolPage.CreateSchool(self.driver)
        crreateschool.set_school_type(1)
        crreateschool.input_name('学校')
        crreateschool.set_period(random.randint(1, 3))
        crreateschool.click_area()
        # 海南省数据有误，增加选择省市区是否成功结果断言
        try:
            crreateschool.set_pca()
            flag = True
        except:
            crreateschool.back()
            flag = False
            crreateschool.click_save()

        self.assertTrue(flag, '选择省市区失败')
        self.assertEqual(crreateschool.get_activity(), '.school.classmanager.CreateClassActivity')

    def test_create_institution(self):
        """创建机构"""
        cs = createschoolPage.CreateSchool(self.driver)
        cs.set_school_type(2)
        cs.input_name('机构')
        cs.click_area()
        # 海南省数据有误，增加选择省市区是否成功结果断言
        try:
            cs.set_pca()
            flag = True
        except:
            cs.back()
            flag = False
        cs.click_save()

        self.assertTrue(flag, '选择省市区失败')
        self.assertEqual(cs.get_activity(), '.school.classmanager.CreateClassActivity')


if __name__ == '__main__':
    unittest.main()
