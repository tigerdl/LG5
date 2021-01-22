from time import sleep

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
    def goto_add_department(self):
        self.find_func(By.CSS_SELECTOR,".js_create_dropdown").click()
        sleep(1)
        self.find_func(By.CSS_SELECTOR,".js_create_party").click()
        # self.driver.find_element(By.CSS_SELECTOR,".js_create_party").click()
        return AddDepartmentPage(self.driver)

    #导入通讯录
    def import_contacts(self):
        pass

    #获取部门列表
    def get_dep_list(self):
        dep_list = self.driver.find_elements(By.CSS_SELECTOR,".jstree-anchor:nth-child(3)")
        dep_name_list = []
        for dep in dep_list:
            dep_name_list.append(dep.text)
        return dep_name_list

