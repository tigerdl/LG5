import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BaseDriver:

    def __init__(self,driver=None):
        driver:WebDriver
        if driver is None:
            self.driver = webdriver.Chrome()
            self._cookie_login()
        else:
            self.driver = driver

    #存取cookie
    def _cookie_login(self):
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

        # cookies = self.driver.get_cookies()
        # with open("cookie.json","w") as f:
        #     json.dump(cookies,f)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # sleep(5)
        with open("cookie.json","r") as f:
            cookies = json.load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.maximize_window()