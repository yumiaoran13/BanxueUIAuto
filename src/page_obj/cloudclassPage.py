from basePage import BaseAction
import configread


class CloudClass(BaseAction):
    """
    云课堂页面
    """
    conf = configread.ConfigRead('控件.ini')
    cloudclass_loc = conf.get_elinfo('学堂', '云课堂')
    class_loc = conf.get_elinfo('云课堂', '班级列表')
    tab_loc = conf.get_elinfo('云课堂', '标签')
    join_loc = conf.get_elinfo('云课堂', '加入')
    schedule_loc = conf.get_elinfo('云课堂', '课表')
    play_loc = conf.get_elinfo('云课堂', '点击观看')
    vip_loc = conf.get_elinfo('云课堂', '开通会员')

    def __init__(self, driver):
        super().__init__(driver)
        self.click(*self.cloudclass_loc)

    # 点击班级列表
    def click_class(self, index):
        self.clicks(*self.class_loc, index=index)

    def switch_tab(self, index):
        """
        切换tab
        :param index: 0云课堂，1课堂回看
        :return:
        """
        if index == 0:
            self.clicks(*self.tab_loc, index=0)
        elif index == 1:
            self.clicks(*self.tab_loc, index=1)
        else:
            print('参数错误')

    # 加入云课堂
    def join_class(self):
        self.click(*self.join_loc)

    def set_schedule(self, day):
        """
        切换课程表
        :param day: 0第一列，1第二列，2第三列...6最后一列
        :return:
        """

        schedules = self.find_elements(*self.schedule_loc)
        schedule = {0: schedules[0], 1: schedules[1], 2: schedules[2], 3: schedules[3], 4: schedules[4],
                    5: schedules[5], 6: schedules[6]}

        if day in schedule.keys():
            schedules[day].click()
        else:
            print('参数错误')

    # 查找状态为可以观看的视频并点击
    def play(self):
        eles = self.find_elements(*self.play_loc)
        for ele in eles:
            if ele.get_attribute('text') == '点击观看':
                ele.click()
                break
            else:
                print('暂无可观看视频')

    # 点击开通会员按钮
    def click_openvip(self):
        self.click(self.vip_loc)
