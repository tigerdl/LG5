# -*- coding: utf-8 -*-
# @Time : 2021/3/11 22:37
# @author :lidong
import os

import yaml


class GetData:
    def __init__(self):
        self.filepath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.inifilepath = self.filepath + r'\test_webwework' + r'\test_request_po' + r'\url.yaml'
        self.testdatafilepath = self.filepath + r'\test_webwework' + r'\test_request_po' + r'\test_data.yaml'

    def get_data(self, filepath):
        with open(filepath, encoding='utf-8') as f:
            r = yaml.safe_load(f)
            # print(r)
            return r


if __name__ == '__main__':
    filepath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    inifilepath = filepath + r'\test_webwework' + r'\test_request_po' + r'\url.yaml'
    testdatafilepath = filepath + r'\test_webwework' + r'\test_request_po' + r'\test_data.yaml'
    getdata = GetData()
    getdata.get_data(testdatafilepath)
