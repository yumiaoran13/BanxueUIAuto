from basePage import BaseAction
import configread
import random


class ChooseSchool(BaseAction):
    """
    选择学校页面
    """
    conf = configread.ConfigRead('控件.ini')
    add_loc = conf.get_elinfo('班级管理', '创建学校')
    search_loc = conf.get_elinfo('班级管理', '搜索学校')
    schools_loc = conf.get_elinfo('班级管理', '学校列表')

    def __init__(self, driver):
        super().__init__(driver)

    def click_add(self):
        self.click(*self.add_loc)

    def click_school(self):
        """
        随机选择列表中学校
        """
        school_list = self.find_elements(*self.schools_loc)
        index = random.randint(0, len(school_list)-1)
        self.clicks(*self.schools_loc, index=index)

    def search(self, name):
        """
        搜索功能
        :param name: 搜索关键字
        :return:
        """
        self.click(*self.search_loc)
        self.send_key(*self.search_loc, value=name)
