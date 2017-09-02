from basePage import BaseAction
import configread
import time
import random


class CreateSchool(BaseAction):
    """
    创建学校页面
    """
    conf = configread.ConfigRead('控件.ini')
    school_loc = conf.get_elinfo('班级管理', '类型学校')
    institution_loc = conf.get_elinfo('班级管理', '类型机构')
    name_loc = conf.get_elinfo('班级管理', '学校名称')
    primary_loc = conf.get_elinfo('班级管理', '学段小学')
    junior_loc = conf.get_elinfo('班级管理', '学段初中')
    high_loc = conf.get_elinfo('班级管理', '学段高中')
    area_loc = conf.get_elinfo('班级管理', '所在区域')
    pca_loc = conf.get_elinfo('班级管理', '选择省市')
    address_loc = conf.get_elinfo('班级管理', '地址')
    save_loc = conf.get_elinfo('班级管理', '保存')
    # 进入页面前置操作元素
    classmanage_loc = conf.get_elinfo('学堂', '班级管理')
    createclass_loc = conf.get_elinfo('班级管理', '创建班级')
    chooseschool_loc = conf.get_elinfo('班级管理', '选择学校')
    add_loc = conf.get_elinfo('班级管理', '创建学校')

    def __init__(self, driver):
        super().__init__(driver)
        self.click(*self.classmanage_loc)
        self.click(*self.createclass_loc)
        self.click(*self.chooseschool_loc)
        self.click(*self.add_loc)

    def set_school_type(self, type):
        """
        选择创建类型：机构或学校
        :param type: 1学校，2机构
        :return:
        """
        if type == 1:
            pass
        elif type == 2:
            self.click(*self.institution_loc)
        else:
            print('参数错误')

    def input_name(self, name):
        now = time.strftime('%Y%m%d%H%M%S')
        fname = name + now
        self.send_keys(*self.name_loc, value=fname)

    def set_period(self, period):
        """
        选择学段
        :param period: 1高中，2初中，3小学
        :return:
        """
        if period == 1:
            pass
        elif period == 2:
            self.click(*self.junior_loc)
        elif period == 3:
            self.click(*self.primary_loc)
        else:
            print('参数错误')

    def click_area(self):
        self.click(*self.area_loc)

    def set_pca(self):
        """
        随机选择学校所在省市区
        """
        while True:
            pca_list = self.find_elements(*self.pca_loc)
            index = random.randint(0, len(pca_list) - 1)
            self.clicks(*self.pca_loc, index=index)
            # print(self.get_activity())
            if self.get_activity() == '.school.classmanager.AddSchoolActivity':
                break

    def click_save(self):
        self.click(*self.save_loc)
