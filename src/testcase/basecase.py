import unittest
import initdriver
from screenshot import screen_shot
import time
import loginPage


class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = initdriver.driver()
        lp = loginPage.Login(self.driver)
        lp.login()

    def tearDown(self):
        time.sleep(3)
        screen_shot(self.driver)
        self.driver.close_app()
        self.driver.quit()
