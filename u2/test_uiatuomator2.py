import time

import allure

from pageobject.u2testpage import u2testpage
@allure.feature('zuidade')
class Testui:
    @allure.story('diyi')
    def test_1ui(self,u2):
        page=u2testpage(u2)
        page.licai_click()
        time.sleep(5)
        page.iknow()
        assert "abc"=="bca"

    @allure.story('dier')
    def test_2ui(self, u2):

        assert "abc" == "bca"

    @allure.story('disan')
    @allure.severity('blocker')
    @allure.issue("http://www.baidu.com")
    @allure.testcase("http://www.testlink.com")
    def test_3ui(self, u2):
        assert "abc" == "bca"


    def test_4ui(self, u2):
        assert "abc" == "abc"
