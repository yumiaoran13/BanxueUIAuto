from basePage import BaseAction
import configread


class CreateClass(BaseAction):
    """
    创建班级页面
    """
    conf = configread.ConfigRead('控件.ini')
    school_loc = conf.get_elinfo('班级管理', '选择学校')
    grade_loc = conf.get_elinfo('班级管理', '选择年级')
    class_loc = conf.get_elinfo('班级管理', '选择班级')
    subject_loc = conf.get_elinfo('班级管理', '选择学科')
    create_loc = conf.get_elinfo('班级管理', '确认创建')

    def __init__(self, driver):
        super().__init__(driver)

    def click_school(self):
        self.click(*self.school_loc)

    def click_grade(self):
        self.click(*self.grade_loc)

    def click_class(self):
        self.click(*self.class_loc)

    def click_create(self):
        self.click(*self.create_loc)
