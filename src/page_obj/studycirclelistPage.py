from basePage import BaseAction
import configread


class StudyCircleList(BaseAction):
    """
    学习圈列表页面
    """
    conf = configread.ConfigRead('控件.ini')
    studycircle_loc = conf.get_elinfo('学习圈', '学习圈')
    praise_loc = conf.get_elinfo('学习圈', '点赞')
    praise_num_loc = conf.get_elinfo('学习圈', '点赞数')
    comment_btn_loc = conf.get_elinfo('学习圈', '评论')
    comment_loc = conf.get_elinfo('学习圈', '评论框')
    send_loc = conf.get_elinfo('学习圈', '发表评论')

    def __init__(self, driver):
        super().__init__(driver)
        self.click_find()
        self.click(*self.studycircle_loc)

    def click_comment(self):
        self.click(*self.comment_btn_loc)

    def input_comment(self, comment):
        self.send_keys(*self.comment_loc, value=comment)
        self.click(*self.send_loc)

    def click_praise(self):
        self.click(*self.praise_loc)

    def get_praisenum(self, index=0):
        """获取列表中某条数据的点赞数，默认第一条"""
        praise_num = int(self.get_attributes(*self.praise_num_loc, index=index, attribute='text'))
        return praise_num
