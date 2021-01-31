# -*- coding: utf-8 -*-
# @Time : 2021/1/31 11:43
# @author :lidong
from test_appium.page.base_page import BasePage
from test_appium.page.market import Market


class Main(BasePage):
    def goto_market(self):
        self.steps("../page/main.yaml")
        return Market(self._driver)