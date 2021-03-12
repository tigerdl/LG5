# -*- coding: utf-8 -*-
# @Time : 2021/3/11 22:35
# @author :lidong
import requests

from test_webwework.test_request_po.get_data import GetData


class Base:
    def __init__(self):
        self.getdata = GetData()
        token_url = self.getdata.get_data(self.getdata.inifilepath).get('get_token_url')
        r = requests.get(token_url)
        self.token = r.json()['access_token']
        self.s = requests.Session()
        self.s.params = {'access_token': self.token}

    def send(self, *args, **kwargs):
        r = self.s.request(*args, **kwargs)
        return r.json()
