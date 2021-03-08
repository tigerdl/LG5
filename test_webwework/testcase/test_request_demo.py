# -*- coding: utf-8 -*-
# @Time : 2021/3/8 21:51
# @author :lidong
import requests


class TestDemo:
    get_token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwf57613d8503cd14e&corpsecret=PVwEO62Zo-C16-WV6u4LxIciWDavHm0_QFWy4WdIg2Q'
    r = requests.get(get_token_url)
    token = r.json()['access_token']

    def test_add_contacts_mem(self):
        add_contacts_mem_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}'
        data = {
            "userid": "lili",
            "name": "ikik",
            "department": [2],
            "mobile": 13000000000
        }
        r = requests.post(add_contacts_mem_url, json=data)
        print(r.json())

    def test_delete_contacts_mem(self):
        delete_contacts_mem_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid=lili'
        requests.get(delete_contacts_mem_url)

    def test_query_contacts_mem(self):
        query_contacts_mem_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid=LiDong'
        r = requests.get(query_contacts_mem_url)
        print(r.json())

    def test_edit_contacts_mem(self):
        edit_contacts_mem_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}'
        data = {
            'userid': "LiDong",
            "name":"haha"
        }
        r = requests.post(edit_contacts_mem_url, json=data)
        print(r.json())
