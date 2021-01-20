from selenium.webdriver.common.by import By

from page.basedriver import BaseDriver
from page.contacts_page import ContactsPage


class HomePage(BaseDriver):
    """
    企业微信首页
    """

    #添加成员
    def add_member(self):
        pass

    #导入通讯录
    def import_contacts(self):
        pass

    def goto_contacts(self):
        self.driver.find_element(By.ID,"menu_contacts").click()
        return ContactsPage