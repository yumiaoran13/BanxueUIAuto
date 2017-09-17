from basePage import BaseAction
import configread


class MicroCourse(BaseAction):
    """
    微课页面
    """
    conf = configread.ConfigRead('控件.ini')
    microcourse_loc = conf.get_elinfo('学堂', '微课')
    grade_loc = conf.get_elinfo('微课', '设置年级')
    grade_list_loc = conf.get_elinfo('微课', '年级列表')
    save_loc = conf.get_elinfo('微课', '保存')
    switch_loc = conf.get_elinfo('微课', '切换教材')
    version_list_loc = conf.get_elinfo('微课', '教材名')
    ok_loc = conf.get_elinfo('微课', '确定')
    version_loc = conf.get_elinfo('微课', '版本名称')
    subject_list_loc = conf.get_elinfo('微课', '学科列表')
    video_list_loc = conf.get_elinfo('微课', '视频列表')
    video_name_loc = conf.get_elinfo('微课', '视频标题')
    topic_list_loc = conf.get_elinfo('微课', '专题列表')
    topic_subject_loc = conf.get_elinfo('微课', '学科tab')

    def __init__(self, driver):
        super().__init__(driver)
        self.click(*self.microcourse_loc)

    def set_grade(self, grade):
        """
        设置年级
        :param grade: 3三年级，4四年级，5五年级，6六年级，7初一，8初二，9初三，10高一，11高二，12高三
        :return:
        """
        self.click(*self.grade_loc)
        grades = self.find_elements(*self.grade_list_loc)
        grade_dict = {3: grades[0], 4: grades[1], 5: grades[2], 6: grades[3], 7: grades[4], 8: grades[5], 9: grades[6],
                      10: grades[7], 11: grades[8], 12: grades[9]}

        if grade in grade_dict.keys():
            grade_dict[grade].click()
        else:
            print('参数错误')
        self.click(*self.save_loc)

    def switch_version(self, version_index, switch_index=2):
        """
        切换教材版本
        :param version_index: 教材版本索引
        :param switch_index: 切换按钮索引
        :return:
        """
        self.clicks(*self.switch_loc, index=switch_index)
        version_list = self.find_elements(*self.version_list_loc)
        if version_index < len(version_list):
            version_list[version_index].click()
        else:
            print('版本不存在')
        self.click(*self.ok_loc)

    # 获取页面当前设置的年级名称
    def get_grade(self):
        grade = self.get_attribute(*self.grade_loc)
        return grade

    # 获取页面当前设置的教材版本名称
    def get_version_name(self, index):
        version_name = self.get_attributes(*self.version_loc, index=index)
        return version_name

    # 点击指定学科
    def click_subject(self, index):
        self.clicks(*self.subject_list_loc, index=index)

    # 点击随机专题
    def click_topic(self):
        self.random_ele(*self.topic_list_loc).click()

    # 点击随机视频
    def click_video(self):
        self.random_ele(*self.video_list_loc).click()

    # 切换专题的学科
    def switch_tab(self, value):
        eles = self.find_elements(*self.topic_subject_loc)
        for ele in eles:
            if ele.get_attribute('text') == value:
                ele.click()
                break
            else:
                print('学科不存在')
