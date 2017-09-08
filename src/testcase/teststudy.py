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
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        value = '这是一条自动发出的只有文字的学习圈' + now
        studycircle.input_content(value)
        studycircle.set_school()
        studycircle.click_create()
        self.assertEqual(studycircle.get_activity(), '.circle.xuexiquan.DongTaiListActivity')

    def test_add_study_picture(self):
        """发布学习圈 :文字＋图片"""
        studycircle = studycirclePage.StudyCircle(self.driver)
        studycircle.click_add()
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        value = '这是一条自动发出的有文字和图片的学习圈' + now
        studycircle.input_content(value)
        studycircle.set_picture()
        studycircle.set_school()
        studycircle.click_create()
        time.sleep(2)
        self.assertEqual(studycircle.get_activity(), '.circle.xuexiquan.DongTaiListActivity')

    @unittest.skip('不同手机相机控件不同')
    def test_add_study_photo(self):
        """发布学习圈 :文字＋照片"""
        studycircle = studycirclePage.StudyCircle(self.driver)
        studycircle.click_add()
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        value = '这是一条自动发出的有文字和相机拍摄照片的学习圈' + now
        studycircle.input_content(value)
        studycircle.take_photo()
        studycircle.set_school()
        studycircle.click_create()
        time.sleep(2)
        self.assertEqual(studycircle.get_activity(), '.circle.xuexiquan.DongTaiListActivity')

    def test_add_study_video(self):
        """发布学习圈 :视频"""
        studycircle = studycirclePage.StudyCircle(self.driver)
        studycircle.click_add()
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        value = '这是一条自动发出的有文字和视频的学习圈' + now
        studycircle.input_content(value)
        studycircle.set_video()
        studycircle.set_school()
        studycircle.click_create()
        time.sleep(2)
        self.assertEqual(studycircle.get_activity(), '.circle.xuexiquan.DongTaiListActivity')

if __name__ == '__main__':
    unittest.main()
