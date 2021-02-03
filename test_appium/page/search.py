# -*- coding: utf-8 -*-
# @Time : 2021/1/31 12:19
# @author :lidong
from test_appium.page.base_page import BasePage


class Search(BasePage):
    def search(self,value):
        self._params["value"] = value
        print(111,self._params)
        self.steps("../page/search.yaml")
