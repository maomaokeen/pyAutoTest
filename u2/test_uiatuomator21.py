import time

from pageobject.u2testpage import u2testpage
class Testui:
    def test_1ui1(self,u2):
        page=u2testpage(u2)
        page.licai_click()
        time.sleep(5)
        page.iknow()
        assert "abc"=="bca"

    def test_2ui1(self, u2):
        assert "abc" == "bca"

    def test_3ui1(self, u2):
        assert "abc" == "bca"

    def test_4ui1(self, u2):
        assert "abc" == "abc"
