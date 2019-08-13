from framework.Base_Page import BasePage

class licaiPage(BasePage):
    #列出所有元素的定位方法和定位
    licai1 = ["xpath", "//android.widget.TextView[@text='理财']"]  # 导航理财
    licai2 = ['id', 'zhongxinjiantou.szkingdom.android.newphone:id/financing_titleText']  # 理财头
    know =['class','handlebusiness-new-alert-btn-single'] #我知道了

    def click_licai1(self):
        self.click(self.licai1)

    def licai2_text(self):
        a=self.find_element(self.licai2).text
        return a

    def know_click(self):
        self.click(self.know)