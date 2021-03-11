# -*- coding: utf-8 -*-
# @Time : 2021/3/8 21:51
# @author :lidong
import requests

from test_webwework.test_request_po.base import Base


class Address(Base):

    def add_contacts_mem(self, userid, name, department, mobile):
        method = 'post'
        add_contacts_mem_url = self.getdata.get_data('add_contacts_mem_url')
        data = {
            "userid": userid,
            "name": name,
            "department": department,
            "mobile": mobile
        }
        return self.send(method, add_contacts_mem_url, json=data)

    def delete_contacts_mem(self, userid):
        method = 'get'
        delete_contacts_mem_url = self.getdata.get_data('delete_contacts_mem_url')
        params = {
            'userid': userid
        }
        return self.send(method, delete_contacts_mem_url, params=params)

    def query_contacts_mem(self, userid):
        method = 'get'
        query_contacts_mem_url = self.getdata.get_data('query_contacts_mem_url')
        params = {
            'userid': userid
        }
        return self.send(method, query_contacts_mem_url, params=params)

    def edit_contacts_mem(self, userid, name):
        method = 'post'
        edit_contacts_mem_url = self.getdata.get_data('edit_contacts_mem_url')
        data = {
            'userid': userid,
            "name": name
        }
        return self.send(method, edit_contacts_mem_url, json=data)
