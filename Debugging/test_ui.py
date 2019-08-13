import os
import getcwd
from framework.u2base import u2base
import uiautomator2 as ui
import time
u2=u2base()
d=u2.u2driver()
'''d=ui.connect('4f367dbe')
d.app_start('zhongxinjiantou.szkingdom.android.newphone')'''
path = os.path.join(getcwd.get_cwd(), 'screenshots/')
rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
screen_name = path + rq + '.png'
d.screenshot(screen_name)
d(text='理财').click()
d.screenshot(screen_name)
d(text='我知道了').wait(timeout=10.0)
d(text='我知道了').click()
d.screenshot(screen_name)
time.sleep(3)
d.app_stop('zhongxinjiantou.szkingdom.android.newphone')