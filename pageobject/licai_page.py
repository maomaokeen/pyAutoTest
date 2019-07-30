from framework.Base_Page import BasePage

class licaiPage(BasePage):
    #列出所有元素的定位方法和定位
    licai1 = ["xpath", "//android.widget.TextView[@text='理财']"]  # 搜索输入框
    licai2 = ['id', 'zhongxinjiantou.szkingdom.android.newphone:id/financing_titleText']  # 搜索按钮

    def click_licai1(self):
        self.find_element(self.licai1)

    def licai2_text(self):
        a=self.find_element(self.licai2).text
        return a