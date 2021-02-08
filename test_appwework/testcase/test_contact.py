# -*- coding: utf-8 -*-
# @Time : 2021/2/3 23:58
# @author :lidong

import pytest
import yaml

from test_appwework.page.app import App


def get_data():
    with open("../testdata/member.yaml", encoding="utf-8") as f:
        data = yaml.safe_load(f)
        add_data = data["add"]
        return add_data


class TestContact:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize("name,gender,phonenum", get_data())
    def test_add_contact(self, name, gender, phonenum):
        # name = "L1"
        # gender = "女"
        # phonenumber = "10000000007"
        toast = self.main.click_addresslist().add_member().addconnect_menual().edit_gender(gender).edit_name(name).edit_phonenum(phonenum).click_save().get_toast()
        assert toast == "添加成功"

# if __name__ == '__main__':
#     # test = TestContact()
#     data = get_data()
#     print(data)
