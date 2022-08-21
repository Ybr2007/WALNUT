import pickle  # 用于加载和保存二进制的设置文件

_settingFilePath = './Setting/Setting.setting'

class _Setting:
    windowGeometry = (0, 0, 800, 600)
    licence: str = ''
    isDarkMode: bool = False
    
    @staticmethod
    def Load():
        try:
            settingObj = pickle.load(open(_settingFilePath, 'rb'))
            return settingObj
        except:
            return _Setting()

    def Save(self):
        pickle.dump(self, open(_settingFilePath, 'wb'), protocol=pickle.HIGHEST_PROTOCOL)


setting : _Setting = None

def Init():
    global setting
    setting = _Setting.Load()