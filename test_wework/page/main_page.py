# -*- coding: utf-8 -*-
# @Time : 2021/2/3 21:24
# @author :lidong

# 点击通讯录
from appium.webdriver.common.mobileby import MobileBy

from test_wework.page.addmember_page import AddmemberPage
from test_wework.page.basepage import BasePage


class MainPage(BasePage):
    def click_addresslist(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return AddmemberPage(self.driver)
