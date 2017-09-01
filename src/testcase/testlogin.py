from basecase import MyTest
import xuetangPage
import unittest


class TestLogin(MyTest):
    """登陆功能"""

    def test_login(self):
        """老师端登陆测试"""
        xt = xuetangPage.XueTang(self.driver)
        # 获取学堂主页标题
        title = xt.get_title(*xt.title_loc)
        print(title)
        self.assertEqual(xt.get_activity(), '.main.MainActivity')
        self.assertEqual(title, '伴学网')


if __name__ == '__main__':
    unittest.main()
