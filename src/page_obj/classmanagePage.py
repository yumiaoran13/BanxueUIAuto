from basePage import BaseAction
import configread


class ClassManage(BaseAction):
    """
    班级管理页面
    """
    conf = configread.ConfigRead('控件.ini')
    joinclass_loc = conf.get_elinfo('班级管理', '加入班级')
    createclass_loc = conf.get_elinfo('班级管理', '创建班级')

    def __init__(self, driver):
        super().__init__(driver)

    def click_joinclass(self):
        self.click(*self.joinclass_loc)

    def click_createclass(self):
        self.click(*self.createclass_loc)