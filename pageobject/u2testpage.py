from framework.u2page import u2page

class u2testpage(u2page):
    licai="理财"
    know="知道了"
    iknow="我知道了"

    def licai_click(self):
        self.click(self.licai)

    def iknow_click(self):
        self.click(self.iknow)