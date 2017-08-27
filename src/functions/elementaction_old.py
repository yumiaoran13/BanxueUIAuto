from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
# import configparser


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, loc):
        """
        元素定位
        :return: element
        """
        ele = None
        try:
            if by == 'id':
                # 显示等待
                WebDriverWait(self.driver, 15).until(lambda driver: self.driver.find_element_by_id(loc))
                ele = self.driver.find_element_by_id(loc)
            elif by == 'name':
                WebDriverWait(self.driver, 15).until(lambda driver: self.driver.find_element_by_name(loc))
                ele = self.driver.find_element_by_name(loc)
            elif by == 'xpath':
                WebDriverWait(self.driver, 15).until(lambda driver: self.driver.find_element_by_xpath(loc))
                ele = self.driver.find_element_by_xpath(loc)
            elif by == 'link_text':
                WebDriverWait(self.driver, 15).until(lambda driver: self.driver.find_element_by_link_text(loc))
                ele = self.driver.find_element_by_link_text(loc)
        except NoSuchElementException:
            print('找不到元素')
        except TimeoutException:
            print('查找元素超时')
        else:
            return ele

    def find_elements(self, by, loc):
        """
        元素定位
        :return: element
        """
        eles = None
        try:
            if by == 'id':
                # 显示等待
                WebDriverWait(self.driver, 15).until(lambda driver: self.driver.find_elements_by_id(loc))
                eles = self.driver.find_elements_by_id(loc)
            elif by == 'name':
                WebDriverWait(self.driver, 15).until(lambda driver: self.driver.find_elements_by_name(loc))
                eles = self.driver.find_elements_by_name(loc)
            elif by == 'xpath':
                WebDriverWait(self.driver, 15).until(lambda driver: self.driver.find_elements_by_xpath(loc))
                eles = self.driver.find_elements_by_xpath(loc)
            elif by == 'link_text':
                WebDriverWait(self.driver, 15).until(lambda driver: self.driver.find_elements_by_link_text(loc))
                eles = self.driver.find_elements_by_link_text(loc)
        except NoSuchElementException:
            print('找不到元素')
        except TimeoutException:
            print('查找元素超时')
        else:
            return eles

    def isexist(self, by, loc):
        """
        判断元素是否存在
        :param by:
        :param loc:
        :return:
        """
        flag = None
        try:
            if by == 'id':
                # 显示等待
                WebDriverWait(self.driver, 15).until(lambda driver: self.driver.find_element_by_id(loc))
                flag = True
            elif by == 'name':
                WebDriverWait(self.driver, 15).until(lambda driver: self.driver.find_element_by_name(loc))
                flag = True
            elif by == 'xpath':
                WebDriverWait(self.driver, 15).until(lambda driver: self.driver.find_element_by_xpath(loc))
                flag = True
            elif by == 'link_text':
                WebDriverWait(self.driver, 15).until(lambda driver: self.driver.find_element_by_link_text(loc))
                flag = True
        except NoSuchElementException:
            flag = False
            print('找不到元素')
        except TimeoutException:
            flag = False
            print('查找元素超时')
        finally:
            return flag

    def click(self, by, loc):
        ele = self.find_element(by, loc)
        ele.click()

    def clicks(self, by, loc, index):
        eles = self.find_elements(by, loc)
        eles[index].click()

    def send_key(self, by, loc, value):
        ele = self.find_element(by, loc)
        ele.clear()
        ele.send_keys(value)

    def set_value(self, by, loc, value):
        ele = self.find_element(by, loc)
        ele.set_value(value)

    def set_text(self, by, loc, value):
        ele = self.find_element(by, loc)
        ele.set_text(value)

    def get_attribute(self, by, loc, attribute):
        """
        获取控件的属性
        :param by:
        :param loc:
        :param attribute:属性类型
        :return: 控件的属性值
        """
        ele = self.find_element(by, loc)
        value = ele.get_attribute(attribute)
        return value

    def getsize(self):
        """
        获取屏幕尺寸
        :return: tuple
        """
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return [x, y]

    def swipe_left(self, during=None):
        l = self.getsize()
        x1 = l[0] * 0.75
        y = l[1] * 0.5
        x2 = l[0] * 0.25
        self.driver.swipe(x1, y, x2, y, during)

    def swipe_right(self, during=None):
        l = self.getsize()
        x1 = l[0] * 0.25
        y = l[1] * 0.5
        x2 = l[0] * 0.75
        self.driver.swipe(x1, y, x2, y, during)

    def swipe_up(self, during=None):
        l = self.getsize()
        x = l[0] * 0.5
        y1 = l[1] * 0.75
        y2 = l[1] * 0.25
        self.driver.swipe(x, y1, x, y2, during)

    def swipe_down(self, during=None):
        l = self.getsize()
        x = l[0] * 0.5
        y1 = l[1] * 0.25
        y2 = l[1] * 0.75
        self.driver.swipe(x, y1, x, y2, during)
