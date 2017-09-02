from basePage import BaseAction
import configread
import random


class StudyCircle(BaseAction):
    """
    学习圈页面
    """
    conf = configread.ConfigRead('控件.ini')
    studycircle_loc = conf.get_elinfo('学习圈', '学习圈')
    add_loc = conf.get_elinfo('学习圈', '添加')
    content_loc = conf.get_elinfo('学习圈', '内容')
    picture_loc = conf.get_elinfo('学习圈', '图片')
    picture_select_loc = conf.get_elinfo('学习圈', '复选框')
    save_picture_loc = conf.get_elinfo('学习圈', '确认图片')
    school_loc = conf.get_elinfo('学习圈', '选择学校')
    school_list_loc = conf.get_elinfo('学习圈', '学校列表')
    create_loc = conf.get_elinfo('学习圈', '发布')

    def __init__(self, driver):
        super().__init__(driver)
        self.click_find()
        self.click(*self.studycircle_loc)

    # 点发布学习圈按钮
    def click_add(self):
        self.click(*self.add_loc)

    def input_content(self, content):
        """
        输入学习圈内容
        :param content: str：学习圈内容
        :return:
        """
        self.send_keys(*self.content_loc, value=content)

    # 随机选择已加入学校
    def set_school(self):
        self.click(*self.school_loc)
        school_list = self.find_elements(*self.school_list_loc)
        index = random.randint(0, len(school_list)-1)
        self.clicks(*self.school_list_loc, index=index)

    # 随机选择相册中9张图片，不足9张则选择全部
    def set_picture(self):
        self.click(*self.picture_loc)

        pictures = self.find_elements(*self.picture_select_loc)
        try:
            select_pictures = random.sample(pictures, 9)
            for select_picture in select_pictures:
                select_picture.click()
        except ValueError:
            for picture in pictures:
                picture.click()
            print('照片不足9张，自动选择相册中所有照片')
        self.click(*self.save_picture_loc)

    # 点击发布
    def click_create(self):
        self.click(*self.create_loc)

