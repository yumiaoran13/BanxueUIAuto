from basePage import BaseAction
import configread


class XueTang(BaseAction):
    """
    学堂主页面
    """
    conf = configread.ConfigRead('控件.ini')
    school_loc = conf.get_elinfo('导航', '学堂')
    communicate_loc = conf.get_elinfo('导航', '沟通')
    find_loc = conf.get_elinfo('导航', '发现')
    my_loc = conf.get_elinfo('导航', '我的')
    sethomework_loc = conf.get_elinfo('学堂', '布置作业')
    checkhomework_loc = conf.get_elinfo('学堂', '批改作业')
    classmanage_loc = conf.get_elinfo('学堂', '班级管理')
    title_loc = conf.get_elinfo('学堂', '标题')

    def __init__(self, driver):
        super().__init__(driver)

    def click_school(self):
        self.click(*self.school_loc)

    def click_communicate(self):
        self.click(*self.communicate_loc)

    def click_find(self):
        self.click(*self.find_loc)

    def click_my(self):
        self.click(*self.my_loc)

    def click_sethomework(self):
        self.click(*self.sethomework_loc)

    def click_checkhomework(self):
        self.click(self.checkhomework_loc)

    def click_classmanage(self):
        self.click(*self.classmanage_loc)
