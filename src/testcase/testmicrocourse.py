from basecase import MyTest
import microcoursePage
import unittest
import random


class TestMicroCourse(MyTest):
    """微课"""

    def test_set_grade(self):
        """设置年级测试"""
        microcourse = microcoursePage.MicroCourse(self.driver)
        microcourse.set_grade(6)
        grade = microcourse.get_grade()
        self.assertEqual(grade, '小学六年级', '年级设置失败')

    def test_topic_list(self):
        """切换教材版本测试"""
        microcourse = microcoursePage.MicroCourse(self.driver)
        microcourse.set_grade(3)
        microcourse.switch_version(1)
        version_name = microcourse.get_version_name(2)
        self.assertEqual(version_name, '北师大版', '版本设置失败')

    def test_xiaoxue_video_list(self):
        """小学微课视频列表测试"""
        microcourse = microcoursePage.MicroCourse(self.driver)
        microcourse.set_grade(6)
        microcourse.click_subject(random.randint(0, 2))
        microcourse.click_video()
        self.assertEqual(microcourse.get_activity(), '.video.WeikePlayActivity')

    def test_middleschool_video_list(self):
        """初中高中微课视频列表测试"""
        microcourse = microcoursePage.MicroCourse(self.driver)
        microcourse.set_grade(random.randint(7, 13))
        microcourse.click_subject(random.randint(0, 6))
        microcourse.click_topic()
        microcourse.click_video()
        self.assertEqual(microcourse.get_activity(), '.video.WeikePlayActivity')

    def test_special_math(self):
        """奥数专题视频列表测试"""
        microcourse = microcoursePage.MicroCourse(self.driver)
        microcourse.set_grade(6)
        microcourse.swipe_up()
        microcourse.click_subject(-2)
        microcourse.click_video()
        self.assertEqual(microcourse.get_activity(), '.video.WeikePlayActivity')

    def test_special_rise(self):
        """小升初专题视频列表测试"""
        microcourse = microcoursePage.MicroCourse(self.driver)
        microcourse.set_grade(6)
        microcourse.swipe_up()
        microcourse.click_subject(-1)
        microcourse.click_topic()
        microcourse.click_video()
        self.assertEqual(microcourse.get_activity(), '.video.WeikePlayActivity')

if __name__ == '__main__':
    unittest.main()
