# -*- coding: utf-8 -*-
# @Time : 2021/2/3 21:33
# @author :lidong

# 编辑成员的信息
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_wework.page.basepage import BasePage


class ContactEditPage(BasePage):

    def edit_name(self, name):
        self.find_and_sendkeys((MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText"), name)
        return self

    def edit_gender(self, gender):
        locator = (MobileBy.XPATH, "//*[@text='男']")
        ele = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        ele.click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        if gender == "女":
            self.find_and_click((MobileBy.XPATH, "//*[@text='女']"))
        else:
            self.find_and_click((MobileBy.XPATH, "//*[@text='男']"))
        return self

    def edit_phonenum(self, phonenum):
        self.find_and_sendkeys((MobileBy.ID, "com.tencent.wework:id/fuy"), phonenum)
        return self

    def click_save(self):
        from test_wework.page.memberinvite_page import MemberInvitePage
        self.find_and_click((MobileBy.ID, "com.tencent.wework:id/ie7"))
        return MemberInvitePage(self.driver)
