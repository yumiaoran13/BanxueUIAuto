from basePage import BaseAction
import configread


class Login(BaseAction):
    """
    登陆页面
    """
    conf = configread.ConfigRead('控件.ini')
    data = configread.ConfigRead('数据.ini')
    start_loc = conf.get_elinfo('启动', '马上体验')
    username_loc = conf.get_elinfo('登陆', '用户名')
    username_value = data.get_value('登陆', '用户名')
    pwd_loc = conf.get_elinfo('登陆', '密码')
    pwd_value = data.get_value('登陆', '密码')
    login_loc = conf.get_elinfo('登陆', '登陆')

    def __init__(self, driver):
        super().__init__(driver)

    def click_start(self):
        for l in range(3):
            self.swipe_left()
        self.click(*self.start_loc)

    def input_username(self):
        self.send_key(*self.username_loc, value=self.username_value)

    def input_pwd(self):
        self.send_key(*self.pwd_loc, value=self.pwd_value)

    def click_login(self):
        self.click(*self.login_loc)

    # 定义统一登陆入口
    def login(self):
        self.click_start()
        self.input_username()
        self.input_pwd()
        self.click_login()
