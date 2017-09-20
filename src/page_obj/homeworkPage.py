from basePage import BaseAction
import configread
import time


class HomeWork(BaseAction):
    """
    布置作业页面
    """
    conf = configread.ConfigRead('控件.ini')
    sethomework_loc = conf.get_elinfo('学堂', '布置作业')
    subject_loc = conf.get_elinfo('布置作业', '选择学科')
    subject_list_loc = conf.get_elinfo('布置作业', '学科列表')
    class_loc = conf.get_elinfo('布置作业', '选择班级')
    grade_list_loc = conf.get_elinfo('布置作业', '年级列表')
    class_list_loc = conf.get_elinfo('布置作业', '班级列表')
    ok_loc = conf.get_elinfo('布置作业', '确定班级')
    version_loc = conf.get_elinfo('布置作业', '选择教材')
    version_list_loc = conf.get_elinfo('布置作业', '版本列表')
    book_list_loc = conf.get_elinfo('布置作业', '册别列表')
    save_version_loc = conf.get_elinfo('布置作业', '确定版本')
    practice_loc = conf.get_elinfo('布置作业', '同步练习')
    point_loc = conf.get_elinfo('布置作业', '知识点')
    chapter_loc = conf.get_elinfo('布置作业', '选择内容')
    chapter_list_loc = conf.get_elinfo('布置作业', '章节列表')
    add_loc = conf.get_elinfo('布置作业', '添加题目')
    preview_loc = conf.get_elinfo('布置作业', '预览')
    set_homework_loc = conf.get_elinfo('布置作业', '布置作业')
    sure_loc = conf.get_elinfo('布置作业', '确认布置')

    def __init__(self, driver):
        super().__init__(driver)
        self.click(*self.sethomework_loc)

    def set_homework_type(self, homework_type):
        """
        设置作业类型
        :param homework_type: 0同步练习1知识点
        :return:
        """
        if homework_type == 0:
            pass
        elif homework_type == 1:
            self.clicks(*self.point_loc)
        else:
            print('参数错误')

    def set_subject(self, subject):
        """
        设置学科
        :param subject: 0语文，1数学，3英语，4物理，5化学，6地理，7历史，8政治，9生物，10信息技术
        :return:
        """
        self.click(*self.subject_loc)
        try:
            self.clicks(*self.subject_list_loc, index=subject)
        except IndexError:
            print('参数错误')

    def set_class(self, index1, index2):
        """
        设置班级
        :param index1: 年级索引
        :param index2: 班级索引
        :return:
        """
        self.click(*self.class_loc)
        try:
            self.clicks(*self.grade_list_loc, index=index1)
            self.clicks(*self.class_list_loc, index=index2)
        except IndexError:
            print('参数错误')
        self.click(*self.ok_loc)

    def set_vertion(self, index1, index2):
        """
        设置教材版本和册别
        :param index1: 版本索引
        :param index2: 册别索引
        :return:
        """

        self.click(*self.version_loc)
        try:
            self.clicks(*self.version_list_loc, index=index1)
            self.clicks(*self.book_list_loc, index=index2)
        except IndexError:
            print('参数错误')
        self.click(*self.save_version_loc)

    # 选择随机章节的随机题目
    def set_question(self):
        self.click(*self.chapter_loc)
        for i in range(10):
            self.random_ele(*self.chapter_list_loc).click()
            time.sleep(10)
            # 随机选择章节，如果所选章节没有题目，返回选择章节页面
            if self.isexists(*self.add_loc):
                self.random_ele(*self.add_loc)
                break
            else:
                self.click_back()

    # 布置作业
    def set_homework(self):
        self.click(*self.set_homework_loc)
        self.click(*self.sure_loc)

    # 预览作业
    def preview(self):
        self.click(*self.preview_loc)


