from basePage import BaseAction
import configread


class ResourcePage(BaseAction):
    """
    资源页面
    """
    # 定位器
    conf = configread.ConfigRead('控件.ini')
    resource_loc = conf.get_elinfo('学堂', '资源')
    filter_loc = conf.get_elinfo('资源', '筛选')
    period_loc = conf.get_elinfo('资源', '学段')
    subject_loc = conf.get_elinfo('资源', '选择学科')
    subject_list_loc = conf.get_elinfo('资源', '学科列表')
    version_loc = conf.get_elinfo('资源', '选择教材')
    version_list_loc = conf.get_elinfo('资源', '教材列表')
    book_loc = conf.get_elinfo('资源', '选择册别')
    book_list_loc = conf.get_elinfo('资源', '册别列表')
    chapter_loc = conf.get_elinfo('资源', '选择章节')
    chapter_list_loc = conf.get_elinfo('资源', '章节列表')
    save_loc = conf.get_elinfo('资源', '完成')

    def __init__(self, driver):
        super().__init__(driver)
        self.click(*self.resource_loc)

    def click_filter(self):
        self.click(*self.filter_loc)

    def set_period(self, period):
        """
        选择学段
        :param period: 3小学，2初中，1高中
        :return:
        """
        if period == 3:
            self.clicks(*self.period_loc, index=0)
        elif period == 2:
            self.clicks(*self.period_loc, index=1)
        elif period == 1:
            self.clicks(*self.period_loc, index=2)
        else:
            print('参数错误')

    def set_subject(self):
        """随机选择学科"""
        self.click(*self.subject_loc)
        self.random_ele(*self.subject_list_loc).click()

    def set_version(self):
        """随机选择教材版本"""
        self.click(*self.version_loc)
        self.random_ele(*self.version_list_loc).click()

    def set_book(self):
        """随机选择册别"""
        self.click(*self.book_loc)
        self.random_ele(*self.book_list_loc).click()

    def set_chapter(self):
        """随机选择册别"""
        self.click(*self.chapter_loc)
        self.random_ele(*self.chapter_list_loc).click()

    def click_save(self):
        self.click(*self.save_loc)
