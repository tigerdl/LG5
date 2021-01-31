# -*- coding: utf-8 -*-
# @Time : 2021/1/31 0:43
# @author :lidong
from appium import webdriver

from test_appium.page.base_page import BasePage
from test_appium.page.main import Main


class App(BasePage):
    def start(self):
        _package = "com.xueqiu.android"
        _activity = ".view.WelcomeActivityAlias"
        if self._driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"]  = _package
            caps["appActivity"] = _activity
            caps["autoGrantPermissions"] = True
            self._driver  = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(5)
        else:
            self._driver.start_activity(_package, _activity)

        return self

    def main(self):
        return Main(self._driver)