from basecase import MyTest
import random
import resourcePage
import unittest
import screenshot


class TestResource(MyTest):
    """学习圈"""
    def test_filter(self):
        """筛选测试"""
        testresource = resourcePage.ResourcePage(self.driver)
        testresource.click_filter()
        screenshot.screen_shot(self.driver)
        period = random.randint(1, 3)
        testresource.set_period(period)
        testresource.set_subject()
        testresource.set_version()
        testresource.set_book()
        screenshot.screen_shot(self.driver)
        testresource.click_save()
        self.assertEqual(testresource.get_activity(), '.school.ziyuan.ZyMainActivity')


if __name__ == '__main__':
    unittest.main()
