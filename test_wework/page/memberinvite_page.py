# -*- coding: utf-8 -*-
# @Time : 2021/2/3 21:29
# @author :lidong

# 点击手动添加
from appium.webdriver.common.mobileby import MobileBy

from test_wework.page.basepage import BasePage
from test_wework.page.contactedit_page import ContactEditPage


class MemberInvitePage(BasePage):
    def addconnect_menual(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        return ContactEditPage(self.driver)

    def get_toast(self):
        res = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']")
        return res.text
