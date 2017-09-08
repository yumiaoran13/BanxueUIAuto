from basePage import BaseAction
import configread
import random


class CreateClass(BaseAction):
    """
    创建班级页面
    """
    conf = configread.ConfigRead('控件.ini')
    school_loc = conf.get_elinfo('班级管理', '选择学校')
    grade_loc = conf.get_elinfo('班级管理', '选择年级')
    grade_list_loc = conf.get_items('年级列表')
    class_loc = conf.get_elinfo('班级管理', '选择班级')
    classname_loc = conf.get_elinfo('班级管理', '班级名称')
    subject_loc = conf.get_elinfo('班级管理', '选择学科')
    subjects_loc = conf.get_elinfo('班级管理', '学科列表')
    sure_loc = conf.get_elinfo('班级管理', '确认')
    create_loc = conf.get_elinfo('班级管理', '确认创建')
    ok_loc = conf.get_elinfo('班级管理', 'ok')
    # 选择学校页面元素
    add_loc = conf.get_elinfo('班级管理', '创建学校')
    search_loc = conf.get_elinfo('班级管理', '搜索学校')
    schools_loc = conf.get_elinfo('班级管理', '学校列表')
    # 进入页面前置操作元素
    classmanage_loc = conf.get_elinfo('学堂', '班级管理')
    createclass_loc = conf.get_elinfo('班级管理', '创建班级')

    def __init__(self, driver):
        super().__init__(driver)
        self.click(*self.classmanage_loc)
        self.click(*self.createclass_loc)

    # 点击选择学校
    def click_school(self):
        self.click(*self.school_loc)

    def set_grade(self):
        """随机选择年级"""
        self.click(*self.grade_loc)
        current_grades = []
        # 将当前页面存在的年级加入新的列表，并随机选择
        for grade in self.grade_list_loc:
            grade = grade[1].split('|')
            if self.isexist(*grade):
                current_grades.append(grade)
        index = len(current_grades) - 1
        self.click(*current_grades[index])

    # 设置班级名称
    def set_classname(self, classname):
        self.click(*self.class_loc)
        self.send_keys(*self.classname_loc, value=classname)
        self.click_sure()

    def set_subject(self, num=1):
        """
        随机选择所授学科
        :param num:选择学科数量
        :return:
        """
        # 点击选择学科
        self.click(*self.subject_loc)

        subject_list = self.find_elements(*self.subjects_loc)
        if num <= len(subject_list):
            for n in range(num):
                index = random.randint(0, len(subject_list)-1)
                self.clicks(*self.subjects_loc, index=index)
                subject_list.pop(index)
        else:
            print('选择学科数不能超过学科总数')

        self.click_sure()

    # 保存所选学科／保存班级名称
    def click_sure(self):
        self.click(*self.sure_loc)

    # 确认创建班级
    def click_create(self):
        self.click(*self.create_loc)

    # 创建成功后点击创建成功提示框
    def click_ok(self):
        self.click(*self.ok_loc)

    def search(self, name):
        """
        选择学校页面搜索功能
        :param name: 搜索关键字
        :return:
        """
        self.click(*self.search_loc)
        self.send_keys(*self.search_loc, value=name)

    # 随机选择列表中的学校
    def set_school(self):
        self.random_ele(*self.schools_loc).click()
