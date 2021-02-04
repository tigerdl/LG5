# -*- coding: utf-8 -*-
# @Time : 2021/2/3 21:33
# @author :lidong

# 编辑成员的信息
from appium.webdriver.common.mobileby import MobileBy


class ContactEditPage:
    def __init__(self, driver):
        self.driver = driver

    def edit_name(self):
        name = "LLL"
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        return self

    def edit_gender(self):
        gender = "男"
        self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        if gender == "女":
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        return self

    def edit_phonenum(self):
        phonenumber = "10000000001"
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/fuy").send_keys(phonenumber)
        return self

    def click_save(self):
        from test_wework.page.memberinvite_page import MemberInvitePage
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ie7").click()
        return MemberInvitePage(self.driver)
