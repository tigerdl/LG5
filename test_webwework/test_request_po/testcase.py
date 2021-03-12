# -*- coding: utf-8 -*-
# @Time : 2021/3/12 0:25
# @author :lidong
import pytest

from test_webwework.test_request_po.get_data import GetData
from test_webwework.test_request_po.request_common import Address


class TestDemo:
    getdata=GetData()
    address = Address()
    # def setUp(self):
    #     self.address = Address()


    @pytest.mark.parametrize('userid, name, department, mobile', GetData().get_data(GetData().testdatafilepath))
    def test_add_contacts_mem(self, userid, name, department, mobile):
        self.address.delete_contacts_mem(userid)
        r = self.address.add_contacts_mem(userid, name, department, mobile)
        res = self.address.query_contacts_mem(userid)
        assert res.get('name', '添加失败') == name

    def test_delete_contacts_mem(self):
        pass

    def test_query_contacts_mem(self):
        pass

    def test_edit_contacts_mem(self):
        pass
