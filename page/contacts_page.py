from selenium.webdriver.common.by import By

from page.add_dep_page import AddDepartmentPage
from page.basedriver import BaseDriver


class ContactsPage(BaseDriver):
    """
    通讯录页面
    """

    #添加成员
    def add_member(self):
        pass

    #添加部门
    def add_department(self):
        self.driver.find_element(By.CSS_SELECTOR,".member_colLeft_top_addBtn").click()
        self.driver.find_element(By.CSS_SELECTOR,".js_create_party").click()
        return AddDepartmentPage

    #导入通讯录
    def import_contacts(self):
        pass

