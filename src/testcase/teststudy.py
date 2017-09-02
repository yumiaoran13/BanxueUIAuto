from basecase import MyTest
import time
import studycirclePage
import unittest


class TestStudy(MyTest):
    """学习圈"""
    def test_add_study_text(self):
        """发布学习圈 :文字"""
        studycircle = studycirclePage.StudyCircle(self.driver)
        studycircle.click_add()
        now = time.strftime('%Y-%m-%d %H-%M-%S')
        value = '这是一条自动发出的只有文字的学习圈' + now
        studycircle.input_content(value)
        studycircle.set_school()
        studycircle.click_create()

    def test_add_study_picture(self):
        """发布学习圈 :文字＋图片"""
        studycircle = studycirclePage.StudyCircle(self.driver)
        studycircle.click_add()
        now = time.strftime('%Y-%m-%d %H-%M-%S')
        value = '这是一条自动发出的有文字和图片的学习圈' + now
        studycircle.input_content(value)
        studycircle.set_picture()
        studycircle.set_school()
        studycircle.click_create()

if __name__ == '__main__':
    unittest.main()
