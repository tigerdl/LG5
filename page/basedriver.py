from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BaseDriver:

    def __init__(self,driver=None):
        driver:WebDriver
        if driver is None:
            self.driver = webdriver.Chrome()
        else:
            self.driver = driver
