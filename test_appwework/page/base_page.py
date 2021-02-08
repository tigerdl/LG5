# -*- coding: utf-8 -*-
# @Time : 2021/2/4 14:19
# @author :lidong
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_and_click(self, locator):
        return self.find(locator).click()

    def find_and_sendkeys(self, locator, value):
        self.find(locator).send_keys(value)

    def scroll_find_click(self, value):
        ele = (MobileBy.ANDROID_UIAUTOMATOR,
               'new UiScrollable(new UiSelector().'
               'scrollable(true).instance(0)).'
               'scrollIntoView(new UiSelector().'
               f'text("{value}").instance(0));')
        self.find_and_click(ele)

    def find_and_gettext(self, locator):
        return self.find(locator).text
