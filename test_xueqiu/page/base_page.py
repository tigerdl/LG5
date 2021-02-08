# -*- coding: utf-8 -*-
# @Time : 2021/2/7 21:44
# @author :lidong
import os
import yaml
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator):
        try:
            return self.driver.find_element(*locator)
        except:
            self.black_list_click()
            return self.find(locator)

    # 获取yaml文件数据->list[dict]
    def get_test_data(self, filename):
        ddata_pathdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + r"\test_data" + "\\" + filename
        with open(ddata_pathdir, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        return data
        # print(data)

    def steps(self, filename):
        datas: list[dict] = self.get_test_data(filename)
        for data in datas:
            if "by" in data.keys():
                ele = self.find((data["by"], data["locator"]))
                if "action" in data.keys():
                    if "click" == data["action"]:
                        ele.click()
                    elif "send" == data["action"]:
                        value: str = data["keys"]
                        ele.send_keys(value)
                        return ele

    def black_list_click(self):
        black_list: list[dict] = self.get_test_data("blackpage.yaml")
        for black in black_list:
            ele=self.steps("blackpage.yaml")
