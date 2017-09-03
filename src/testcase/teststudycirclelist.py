from basecase import MyTest
import time
import studycirclelistPage
import unittest


class TestStudyCirCle(MyTest):
    """学习圈列表"""
    def test_comment(self):
        """发布学习圈评论"""
        studycirclelist = studycirclelistPage.StudyCircleList(self.driver)
        studycirclelist.click_comment()
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        value = '这是一条自动发出的学习圈评论' + now
        studycirclelist.input_comment(value)

    def test_praise(self):
        """点赞、取消点赞"""
        studycirclelist = studycirclelistPage.StudyCircleList(self.driver)
        num = studycirclelist.get_praisenum()
        studycirclelist.click_praise()
        current_num = studycirclelist.get_praisenum()
        self.assertEqual(num - current_num, 1 or -1, '点赞或取消点赞失败')

if __name__ == '__main__':
    unittest.main()
