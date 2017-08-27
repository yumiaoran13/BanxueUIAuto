from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    """基础操作类"""
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
        except NoSuchElementException:
            print('找不到元素')
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
        except NoSuchElementException:
            print('找不到元素')
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
            WebDriverWait(self.driver, 15).until(lambda driver: self.driver.find_element(*loc))
            flag = True
        except NoSuchElementException:
            flag = False
            print('找不到元素')
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

    def send_key(self, *loc, value):
        ele = self.find_element(*loc)
        ele.clear()
        ele.send_keys(value)

    def get_attribute(self, *loc, attribute):
        """
        获取控件的属性
        :param loc:
        :param attribute:属性类型
        :return: str:控件属性值
        """
        ele = self.find_element(*loc)
        value = ele.get_attribute(attribute)
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

    def scroll_to(self, *loc, text):
        pass


