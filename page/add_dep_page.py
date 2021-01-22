from time import sleep

from selenium.webdriver.common.by import By

from page.basedriver import BaseDriver
# from page.contacts_page import ContactsPage


class AddDepartmentPage(BaseDriver):
    """
    添加部门页面
    """

    #添加部门
    def add_department(self,dep_name):
        self.find_func(By.XPATH,'//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[1]/input').send_keys(dep_name)
        self.find_func(By.XPATH,'//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[3]/a').click()
        self.find_func(By.CSS_SELECTOR, '#__dialog__MNDialog__ [id="1688854136113206_anchor"]').click()
        self.find_func(By.CSS_SELECTOR,'[d_ck=submit]').click()
        sleep(2)
        from page.contacts_page import ContactsPage
        return ContactsPage(self.driver)
