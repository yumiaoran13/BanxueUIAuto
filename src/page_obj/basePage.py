# from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.touch_actions import TouchActions
import configread
import random


class BaseAction:
    """基础操作类"""
    conf = configread.ConfigRead('控件.ini')
    study_loc = conf.get_elinfo('导航', '学堂')
    communicate_loc = conf.get_elinfo('导航', '沟通')
    find_loc = conf.get_elinfo('导航', '发现')
    my_loc = conf.get_elinfo('导航', '我的')

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc):
        """
        元素定位
        :return: element
        """
        # ele = None
        try:
            # 显示等待
            WebDriverWait(self.driver, 15).until(lambda driver: self.driver.find_element(*loc))
            ele = self.driver.find_element(*loc)
        # except NoSuchElementException:
            # print('找不到元素')
        except TimeoutException:
            print('查找元素超时')
        else:
            return ele

    def find_elements(self, *loc):
        """
        定位一组元素
        :return: element
        """
        # eles = None
        try:
            WebDriverWait(self.driver, 15).until(lambda driver: self.driver.find_elements(*loc))
            eles = self.driver.find_elements(*loc)
        # except NoSuchElementException:
            # print('找不到元素')
        except TimeoutException:
            print('查找元素超时')
        else:
            return eles

    def isexist(self, *loc):
        """
        判断元素是否存在
        :param loc:
        :return:Boolean
        """
        flag = None
        try:
            # 显示等待
            WebDriverWait(self.driver, 5).until(lambda driver: self.driver.find_element(*loc))
            flag = True
        # except NoSuchElementException:
            # flag = False
            # print('找不到元素')
        except TimeoutException:
            flag = False
            print('查找元素超时')
        finally:
            return flag

    def click(self, *loc):
        ele = self.find_element(*loc)
        ele.click()

    def clicks(self, *loc, index):
        eles = self.find_elements(*loc)
        eles[index].click()

    def long_press(self, *loc, duration=10000):
        ele = self.find_element(*loc)
        elx = ele.location.get('x')
        ely = ele.location.get('y')
        self.driver.swipe(elx, ely, elx, ely, duration=duration)

    def getsize(self):
        """
        获取屏幕尺寸
        :return: tuple
        """
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return [x, y]

    def swipe_left(self, during=None):
        """
        左滑
        :param during:
        :return:
        """
        l = self.getsize()
        x1 = l[0] * 0.75
        y = l[1] * 0.5
        x2 = l[0] * 0.25
        self.driver.swipe(x1, y, x2, y, during)

    def swipe_right(self, during=None):
        """
        右滑
        :param during:
        :return:
        """
        l = self.getsize()
        x1 = l[0] * 0.25
        y = l[1] * 0.5
        x2 = l[0] * 0.75
        self.driver.swipe(x1, y, x2, y, during)

    def swipe_up(self, during=None):
        """
        上滑
        :param during:
        :return:
        """
        l = self.getsize()
        x = l[0] * 0.5
        y1 = l[1] * 0.75
        y2 = l[1] * 0.25
        self.driver.swipe(x, y1, x, y2, during)

    def swipe_down(self, during=None):
        """
        下滑
        :param during:
        :return:
        """
        l = self.getsize()
        x = l[0] * 0.5
        y1 = l[1] * 0.25
        y2 = l[1] * 0.75
        self.driver.swipe(x, y1, x, y2, during)

    def send_keys(self, *loc, value):
        ele = self.find_element(*loc)
        ele.clear()
        ele.send_keys(value)

    def get_attribute(self, *loc, attribute):
        """
        获取一个控件的属性
        :param loc:
        :param attribute:属性类型
        :return: str
        """
        ele = self.find_element(*loc)
        value = ele.get_attribute(attribute)
        return value

    def get_attributes(self, *loc, index, attribute):
        """
        获取一组元素中某一个元素的属性
        :param loc:
        :param index: 元素索引
        :param attribute: 属性类型
        :return: str
        """
        eles = self.find_elements(*loc)
        value = eles[index].get_attribute(attribute)
        return value

    def get_title(self, *loc):
        """
        获取页面标题
        :param loc: 页面控件信息
        :return: str
        """
        title = self.get_attribute(*loc, attribute='text')
        return title

    def get_activity(self):
        activity = self.driver.current_activity
        return activity

    def click_back(self):
        """点击系统返回按钮"""
        self.driver.keyevent(4)

    def random_ele(self, *loc):
        """获取一组元素中随机一个元素"""
        eles = self.find_elements(*loc)
        randele = random.choice(eles)
        return randele

    def click_study(self):
        self.click(*self.study_loc)

    def click_communicate(self):
        self.click(*self.communicate_loc)

    def click_find(self):
        self.click(*self.find_loc)

    def click_my(self):
        self.click(*self.my_loc)
