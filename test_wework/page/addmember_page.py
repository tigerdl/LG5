# -*- coding: utf-8 -*-
# @Time : 2021/2/3 21:27
# @author :lidong

# 点击添加成员
from appium.webdriver.common.mobileby import MobileBy

from test_wework.page.memberinvite_page import MemberInvitePage


class AddmemberPage():
    def __init__(self, driver):
        self.driver = driver

    def add_member(self):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("添加成员").instance(0));').click()
        return MemberInvitePage(self.driver)
