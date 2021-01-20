from selenium import webdriver


class BaseDriver:

    def __init__(self):
        self.driver = webdriver.Chrome()
