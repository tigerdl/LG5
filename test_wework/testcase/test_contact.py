# -*- coding: utf-8 -*-
# @Time : 2021/2/3 23:58
# @author :lidong
import pytest

from test_wework.page.app import App


class TestContact:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()
    @pytest.mark.parametrize("name,gender,phonenum",[["L2","男","10000000008"],["L3","女","10000000009"]])
    def test_add_contact(self,name,gender,phonenum):
        # name = "L1"
        # gender = "女"
        # phonenumber = "10000000007"
        toast = self.main.click_addresslist().add_member().addconnect_menual().edit_gender(gender).edit_name(name).edit_phonenum(phonenum).click_save().get_toast()
        assert toast == "添加成功"