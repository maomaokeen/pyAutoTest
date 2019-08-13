import os
import sys
import time

current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)
import pytest
import uiautomator2 as ui

case_path="./u2/"

@pytest.fixture(scope='module',autouse=True)
def u2():
    global d
    d=ui.connect('4f367dbe')
    d.app_start('zhongxinjiantou.szkingdom.android.newphone')
    return d
@pytest.fixture(scope='module',autouse=True)
def u2_close():
    yield d
    d.app_stop('zhongxinjiantou.szkingdom.android.newphone')

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = "../screenshots/"+report.nodeid.replace("::", "_")+".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:596px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    """

    :param case_name: 用例名
    :return:
    """
    global d
    d.screenshot(name)

