# -*- coding: utf-8 -*-
# @Time : 2021/2/7 20:50
# @author :lidong
from appium.webdriver.common.mobileby import MobileBy

from test_xueqiu.app import App


class TestSearch:

    def setup(self):
        self.app = App()
        self.main = self.app.start().main()

    def test_search(self):
        #测试之前模拟黑名单弹框（点击消息）
        self.main.find((MobileBy.ID, "com.xueqiu.android:id/action_message")).click()
        ele = self.main.goto_search().search()
        assert ele.text == "hello"

    def teardown(self):
        self.app.quit()
