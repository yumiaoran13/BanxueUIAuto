from basecase import MyTest
import cloudclassPage
import unittest
import time


class CloudClass(MyTest):
    """云课堂"""
    def test_join_cloudclass(self):
        """加入演示教室云课堂"""
        cloudclass = cloudclassPage.CloudClass(self.driver)
        cloudclass.swipe_bottom(*cloudclass.class_loc)
        cloudclass.click_class(-1)
        cloudclass.join_class()
        time.sleep(15)
        self.assertEqual(cloudclass.get_activity(), '.school.yunclassroom.InteractiveClassroomActivity', '加入云课堂失败')

    def test_play_video(self):
        """播放课堂回看"""
        cloudclass = cloudclassPage.CloudClass(self.driver)
        cloudclass.swipe_bottom(*cloudclass.class_loc)
        cloudclass.click_class(-1)
        cloudclass.switch_tab(1)
        cloudclass.set_schedule(0)
        cloudclass.play()
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()
