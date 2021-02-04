# -*- coding: utf-8 -*-
# @Time : 2021/2/3 21:21
# @author :lidong

#启动appp、关闭app、重启App、进入首页。。。
from appium import webdriver

from test_wework.page.main_page import MainPage


class App:
    def start(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "wework"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        # 不清空本地缓存，启动app
        caps["noReset"] = "true"
        caps["ensureWebviewsHavePages"] = True
        # 设置页面等待空闲状态的时间为0秒
        caps["settings[waitForIdleTimeout]"] = 1
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
        return self

    def restart(self):
        return self

    def stop(self):
        return self

    def goto_main(self)->MainPage:
        return MainPage(self.driver)