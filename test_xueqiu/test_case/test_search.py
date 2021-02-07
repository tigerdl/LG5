# -*- coding: utf-8 -*-
# @Time : 2021/2/7 20:50
# @author :lidong
from test_xueqiu.app import App


class TestSearch:
    def setup(self):
        self.app = App()
        self.main = self.app.start().main()

    def test_search(self):
        ele = self.main.goto_search().search()
        assert ele.text == "hello"
