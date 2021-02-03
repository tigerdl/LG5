# -*- coding: utf-8 -*-
# @Time : 2021/2/2 21:43
# @author :lidong


# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWeWork:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "wework"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        #不清空本地缓存，启动app
        caps["noReset"] = "true"
        caps["ensureWebviewsHavePages"] = True
        #设置页面等待空闲状态的时间为0秒
        caps["settings[waitForIdleTimeout]"] = 0
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_wework(self):
        el1 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.TextView")
        el1.click()
        el2 = self.driver.find_element_by_id("com.tencent.wework:id/ie_")
        el2.click()
        el5 = self.driver.find_element_by_id("com.tencent.wework:id/gwt")
        el5.send_keys("李东")
        el6 = self.driver.find_element_by_id("com.tencent.wework:id/dsm")
        el6.click()
        el7 = self.driver.find_element_by_id("com.tencent.wework:id/alm")
        el7.click()
        el9 = self.driver.find_element_by_id("com.tencent.wework:id/etm")
        el9.send_keys("hello 李东")
        el10 = self.driver.find_element_by_id("com.tencent.wework:id/eti")
        el10.click()

    def test_autoclick(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='工作台']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='打卡']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'次外出')]").click()
        res = self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/pt")
        assert res.text == "外出打卡成功"

    def test_addmember(self):
        name = "lili"
        gender = "男"
        phonenumber = "15555555555"
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        # self.driver.find_element(MobileBy.XPATH,"//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='手动输入添加']").click()
        #输入名字
        # self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/ern']//*[@class='android.widget.EditText']").send_keys("lili")
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        #选择性别
        # self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/er7']//*[@class='android.widget.ImageView']").click()
        # self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/boi']//*[@text='男']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='男']").click()
        if gender == "女":
            self.driver.find_element(MobileBy.XPATH,"//*[text='女']").click()
        else:
            self.driver.find_element(MobileBy.XPATH,"//*[text='男']").click()
        #输入电话
        # self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/f5y']//*[@class='android.widget.EditText']").send_keys("15555555555")
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/eq7").send_keys(phonenumber)
        #输入邮箱
        # self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/er1']//*[@class='android.widget.EditText']").send_keys("00000000@qq.com")
        #保存
        # self.driver.find_element(MobileBy.XPATH,"//*[@text='保存']").click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/qur").click()
        #断言toast
        res = self.driver.find_element(MobileBy.XPATH,"//*[@class='android.widget.Toast']")
        assert res.text == "添加成功"