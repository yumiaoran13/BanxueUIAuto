from basecase import MyTest
import homeworkPage
import unittest


class HomeWork(MyTest):
    """布置作业"""
    def test_set_homework(self):
        """按同步练习布置"""
        homework = homeworkPage.HomeWork(self.driver)
        homework.set_subject(0)
        homework.set_class(0, 0)
        homework.set_vertion(3, 2)
        homework.set_question()
        homework.set_homework()

if __name__ == '__main__':
    unittest.main()
