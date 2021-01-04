from time import sleep

from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Register(BasePage):
    def register(self):
        self.find(By.ID,"corp_name").send_keys("hello")
        sleep(2)
        self.find(By.ID,"manager_name").send_keys("dong")
        return True
