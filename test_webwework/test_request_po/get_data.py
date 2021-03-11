# -*- coding: utf-8 -*-
# @Time : 2021/3/11 22:37
# @author :lidong
import os

import yaml


class GetData:
    filepath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    inifilepath = filepath + r'\test_webwework' + r'\test_request_po' + r'\url.yaml'

    def get_data(self, url_name):
        with open(self.inifilepath, 'r', encoding='utf-8') as f:
            r = yaml.safe_load(f)
            # print(r.get(url_name, 'url不存在'))
            return r.get(url_name, 'url不存在')


if __name__ == '__main__':
    getdata = GetData()
    getdata.get_data('get_token_url')
