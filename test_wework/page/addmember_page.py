# -*- coding: utf-8 -*-
# @Time : 2021/2/3 21:27
# @author :lidong

# 点击添加成员
from appium.webdriver.common.mobileby import MobileBy

from test_wework.page.basepage import BasePage
from test_wework.page.memberinvite_page import MemberInvitePage


class AddmemberPage(BasePage):
    def add_member(self):
        self.scroll_find_click("添加成员")
        return MemberInvitePage(self.driver)
