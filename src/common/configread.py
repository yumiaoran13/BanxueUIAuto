import os
import configparser


# 获取工程路径
prjdir = os.path.dirname(os.path.dirname((os.path.dirname(__file__))))
path = os.path.join(prjdir + '\config\\')


class ConfigRead:
    """读取配置文件类"""
    def __init__(self, filename):
        self.filename = filename
        self.file_path = path + self.filename
        self.conf = configparser.ConfigParser()

    def get_elinfo(self, section, option):
        """
        读取控件信息
        :param section: section
        :param option: option
        :return: list
        """
        eleinfo = self.get_value(section, option)
        return eleinfo.split('|')

    def get_value(self, section, option):
        """
        重新封装configparser的get方法
        :param section: section
        :param option: option
        :return: str
        """
        self.conf.read(self.file_path, 'utf-8')
        value = self.conf.get(section, option)
        return value

    def get_items(self, section):
        self.conf.read(self.file_path, 'utf-8')
        dict = self.conf.items(section)
        return dict
if __name__ == '__main__':
    e1 = ConfigRead('控件.ini').get_elinfo('启动', '马上体验')
    e2 = ConfigRead('数据.ini').get_value('登陆', '密码')
    print(e1)
    print(e2)
