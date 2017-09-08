from basecase import MyTest
import createschoolPage
import unittest
import random


class TestCreateSchool(MyTest):
    """创建学校"""
    def test_create_school(self):
        """创建学校"""
        createschool = createschoolPage.CreateSchool(self.driver)
        createschool.set_school_type(1)
        createschool.input_name('学校')
        createschool.set_period(random.randint(1, 3))
        # 海南省数据有误，增加选择省市区是否成功结果断言
        try:
            createschool.set_pca()
            flag = True
        except:
            flag = False
        createschool.click_save()

        self.assertTrue(flag, '选择省市区失败')
        self.assertEqual(createschool.get_activity(), '.school.classmanager.CreateClassActivity')

    def test_create_institution(self):
        """创建机构"""
        cs = createschoolPage.CreateSchool(self.driver)
        cs.set_school_type(2)
        cs.input_name('机构')
        # 海南省数据有误，增加选择省市区是否成功结果断言
        try:
            cs.set_pca()
            flag = True
        except:
            flag = False
        cs.click_save()

        self.assertTrue(flag, '选择省市区失败')
        self.assertEqual(cs.get_activity(), '.school.classmanager.CreateClassActivity')


if __name__ == '__main__':
    unittest.main()
