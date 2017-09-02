from basePage import BaseAction
import configread


class XueTang(BaseAction):
    """
    学堂主页面
    """
    conf = configread.ConfigRead('控件.ini')
    sethomework_loc = conf.get_elinfo('学堂', '布置作业')
    checkhomework_loc = conf.get_elinfo('学堂', '批改作业')
    classmanage_loc = conf.get_elinfo('学堂', '班级管理')
    title_loc = conf.get_elinfo('学堂', '标题')

    def __init__(self, driver):
        super().__init__(driver)

    def click_sethomework(self):
        self.click(*self.sethomework_loc)

    def click_checkhomework(self):
        self.click(self.checkhomework_loc)

    def click_classmanage(self):
        self.click(*self.classmanage_loc)
