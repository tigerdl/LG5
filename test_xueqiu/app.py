# -*- coding: utf-8 -*-
# @Time : 2021/2/7 10:36
# @author :lidong
from appium import webdriver

from test_xueqiu.base_page import BasePage
from test_xueqiu.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            caps["noReset"] = "true"
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(10)
        else:
            self.driver.launch_app()
        return self

    def main(self):
        return MainPage(self.driver)
