from time import sleep

from selenium.webdriver.common.by import By

from test_webwework.page.basedriver import BaseDriver
# from page.contacts_page import ContactsPage
from test_webwework.page.contacts_page import ContactsPage


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
        self.find_func(By.ID,"menu_contacts").click()
        sleep(3)
        return ContactsPage(self.driver)