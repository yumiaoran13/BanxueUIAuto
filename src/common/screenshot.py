import configread
import time


def screen_shot(driver):
    now = time.strftime('%Y-%m-%d %H-%M-%S')
    filename = now + '.jpg'
    file_path = configread.prjdir + '\screenshot\\' + filename
    driver.get_screenshot_as_file(file_path)
