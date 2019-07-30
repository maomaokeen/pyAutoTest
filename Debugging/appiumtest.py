#coding = utf-8
import os
import time
from appium import webdriver
#name=zhongxinjiantou.szkingdom.android.newphone
#aname=com.szkingdom.android.phone.ZXJTKdsInitActivity
import getcwd

path = getcwd.get_cwd()
app_path = os.path.join(path, 'app/zhongxinjiantou.szkingdom.android.newphone_4.3.1_431.apk')

desired_caps={
    'platformName':'Android',
    'deviceName':'4f367dbe', #手机设备名称，通过adb devices查看
    'platformVersion':'9', #android系统的版本号
    'app':app_path,
    'appPackage':'zhongxinjiantou.szkingdom.android.newphone',#apk包名
    'appActivity':'com.szkingdom.android.phone.ZXJTKdsInitActivity', #apk的launcherActivity
}

driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

time.sleep(10)

driver.find_element_by_xpath("//android.widget.TextView[@text='理财']").click()
time.sleep(10)
a=driver.find_element_by_id('zhongxinjiantou.szkingdom.android.newphone:id/financing_titleText').text
if a=='理财':
    print('进入了理财页面')
else:
    print('没有进入理财页面')
time.sleep(10)
driver.find_element_by_android_uiautomator('new UiSelector().description("定期理财")').click()
time.sleep(10)
b=driver.find_element_by_xpath("//android.widget.TextView[@text='定期理财']").text
if b=='定期理财':
    print('进入定期理财页面成功')
else:
    print('进入定期理财页面失败')
time.sleep(10)
driver.quit()

