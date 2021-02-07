# -*- coding: utf-8 -*-
# @Time : 2021/2/7 19:46
# @author :lidong
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

from test_xueqiu.base_page import BasePage


class SearchPage(BasePage):
    def search(self):
        ele = self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text")
        ele.send_keys("hello")
        return ele
