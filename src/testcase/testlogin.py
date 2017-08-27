from basecase import MyTest
import loginPage
import xuetangPage
import unittest


class TestLogin(MyTest):
    """登陆功能"""
    def user_login(self):
        lp = loginPage.Login(self.driver)
        lp.login()

    def test_login(self):
        """老师端登陆测试"""
        self.user_login()
        xt = xuetangPage.XueTang(self.driver)
        # 获取学堂主页标题
        title = xt.get_title(*xt.title_loc)
        print(title)
        # 对当前activity和标题断言，数据后续要分离到配置文件
        self.assertEqual(xt.get_activity(), '.main.MainActivity')
        self.assertEqual(title, '伴学网')


if __name__ == '__main__':
    unittest.main()
