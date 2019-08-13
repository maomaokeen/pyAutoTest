import uiautomator2 as u2
class u2base():
    def __int__(self,d):
        self.d=d

    def u2driver(self):
        self.d = u2.connect('4f367dbe')
        self.d.app_start('zhongxinjiantou.szkingdom.android.newphone')
        return self.d
