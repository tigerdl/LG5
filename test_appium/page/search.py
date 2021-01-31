# -*- coding: utf-8 -*-
# @Time : 2021/1/31 12:19
# @author :lidong
from test_appium.page.base_page import BasePage


class Search(BasePage):
    def search(self,value):
        self._params["value"] = value
        self.steps("../page/search.yaml")
