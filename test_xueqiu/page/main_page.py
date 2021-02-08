# -*- coding: utf-8 -*-
# @Time : 2021/2/7 15:15
# @author :lidong
from appium.webdriver.common.mobileby import MobileBy

from test_xueqiu.page.base_page import BasePage
from test_xueqiu.page.search_page import SearchPage


class MainPage(BasePage):
    def goto_search(self):
        # self.find((MobileBy.ID, "com.xueqiu.android:id/tv_search")).click()
        self.steps("mainpage.yaml")
        return SearchPage(self.driver)
