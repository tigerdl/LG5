# -*- coding: utf-8 -*-
# @Time : 2021/2/7 21:44
# @author :lidong
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver
