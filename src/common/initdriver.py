import configread
from appium import webdriver


def driver():
    appconf = configread.ConfigRead('appconf.ini')
    desired_caps = dict(appconf.get_items('desired_caps'))
    dr = webdriver.Remote(appconf.get_value('appium', 'base_url'), desired_caps)
    return dr

if __name__ == '__main__':
    dr = driver()
    dr.quit()
