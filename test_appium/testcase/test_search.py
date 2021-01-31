# -*- coding: utf-8 -*-
# @Time : 2021/1/31 12:34
# @author :lidong
from test_appium.page.app import App


class TestSearch:
    def test_search(self):
        App().start().main().goto_market().goto_search().search("jd")