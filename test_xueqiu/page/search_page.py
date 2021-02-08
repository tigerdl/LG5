# -*- coding: utf-8 -*-
# @Time : 2021/2/7 19:46
# @author :lidong
from appium.webdriver.common.mobileby import MobileBy

from test_xueqiu.page.base_page import BasePage


class SearchPage(BasePage):
    def search(self):
        # ele = self.find((MobileBy.ID, "com.xueqiu.android:id/search_input_text"))
        ele = self.steps("searchpage.yaml")
        # ele.send_keys("hello")
        return ele
