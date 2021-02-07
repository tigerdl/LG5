# -*- coding: utf-8 -*-
# @Time : 2021/2/7 15:15
# @author :lidong
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from test_xueqiu.base_page import BasePage
from test_xueqiu.page.search_page import SearchPage


class MainPage(BasePage):
    def goto_search(self):
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search").click()
        return SearchPage(self.driver)
