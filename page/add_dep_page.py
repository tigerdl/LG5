from time import sleep

from selenium.webdriver.common.by import By

from page.basedriver import BaseDriver
from page.contacts_page import ContactsPage


class AddDepartmentPage(BaseDriver):
    """
    添加部门页面
    """

    #添加部门
    def add_department(self):
        self.driver.find_element(By.CSS_SELECTOR,".ww_inputText").send_keys("部门1")
        self.driver.find_element(By.CSS_SELECTOR,".jstree-anchor").click()
        self.driver.find_element(By.CSS_SELECTOR,".ww_btn_Blue").click()
        sleep(2)
        return ContactsPage
