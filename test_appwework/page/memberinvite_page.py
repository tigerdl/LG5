# -*- coding: utf-8 -*-
# @Time : 2021/2/3 21:29
# @author :lidong

# 点击手动添加
from appium.webdriver.common.mobileby import MobileBy

from test_appwework.page.base_page import BasePage
from test_appwework.page.contactedit_page import ContactEditPage


class MemberInvitePage(BasePage):
    def addconnect_menual(self):
        self.find_and_click((MobileBy.XPATH, "//*[@text='手动输入添加']"))
        return ContactEditPage(self.driver)

    def get_toast(self):
        res = self.find_and_gettext((MobileBy.XPATH, "//*[@class='android.widget.Toast']"))
        return res
