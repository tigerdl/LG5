# -*- coding: utf-8 -*-
# @Time : 2021/1/31 12:14
# @author :lidong
from test_appium.page.base_page import BasePage
from test_appium.page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.steps("../page/market.yaml")
        return Search(self._driver)