import time

from pageobject.u2testpage import u2testpage
class Testui:
    def test_1ui(self,u2):
        page=u2testpage(u2)
        page.licai_click()
        time.sleep(5)
        page.iknow()
        assert "abc"=="bca"

    def test_2ui(self, u2):
        assert "abc" == "bca"

    def test_3ui(self, u2):
        assert "abc" == "bca"

    def test_4ui(self, u2):
        assert "abc" == "abc"
