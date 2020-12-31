import os
# configparser 读取配置的模块 ini
import configparser


class Config(object):
    def __init__(self, config_file='config.ini'):
        self._path = os.path.join(os.getcwd(), config_file)
        if not os.path.exists(self._path):
            raise FileNotFoundError("No such file: config.ini")

        # 生成config对象 支持变量解析
        self._config = configparser.ConfigParser()
        # 直接读取ini文件内容
        self._config.read(self._path, encoding='utf-8-sig')

        # 最基础的INI文件读取类 区分上一个解析
        self._configRaw = configparser.RawConfigParser()
        self._configRaw.read(self._path, encoding='utf-8-sig')

    def get(self, section, name):
        return self._config.get(section, name)

    def getRaw(self, section, name):
        return self._configRaw.get(section, name)


global_config = Config()
