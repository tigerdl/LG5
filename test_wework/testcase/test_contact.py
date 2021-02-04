# -*- coding: utf-8 -*-
# @Time : 2021/2/3 23:58
# @author :lidong
from test_wework.page.app import App


class TestContact:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    def test_add_contact(self):
        toast = self.main.click_addresslist().add_member().addconnect_menual().edit_gender().edit_name().edit_phonenum().click_save().get_toast()
        assert toast == "添加成功"