# -*- coding:utf-8 -*-
import pytest
from libs.member_management import MemberManagement
from common.BaseApi import BaseAssert
from configs.dir_path import report_path
import os
import allure
import allure_pytest


class TestMember(BaseAssert):
    def test_read_member(self, access_token_init, member_init):
        res = member_init.read_member()
        except_data = {'errmsg': 'ok'}
        self.define_assert(res['errmsg'], except_data['errmsg'])


if __name__ == '__main__':
    # pytest.main(['-vs', 'test_member.py'])
    pytest.main(['-s', 'test_member.py', f'--alluredir={report_path}'])
    # os.system(f'allure generate ../report/temp -0 ../reports')