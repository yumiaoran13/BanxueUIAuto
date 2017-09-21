from basecase import MyTest
import homeworkPage
import unittest
import screenshot


class HomeWork(MyTest):
    """布置作业"""
    def test_homework_practice(self):
        """按同步练习布置"""
        homework = homeworkPage.HomeWork(self.driver)
        homework.set_subject(0)
        homework.set_class(0, 0)
        homework.set_vertion(3, 2)
        screenshot.screen_shot(self.driver)
        homework.set_question()
        homework.set_homework()
        self.assertEqual(homework.get_activity(), '.school.layouttask.SureLayoutActivity')

    def test_homework_point(self):
        """按知识点布置"""
        homework = homeworkPage.HomeWork(self.driver)
        homework.set_subject(0)
        homework.set_class(0, 0)
        homework.set_homework_type(1)
        homework.set_question()
        homework.set_homework()
        self.assertEqual(homework.get_activity(), '.school.layouttask.SureLayoutActivity')

if __name__ == '__main__':
    unittest.main()
