# -*- coding:utf-8 -*-
import pytest
from libs.login_token import get_access_token
from libs.member_management import MemberManagement


@pytest.fixture(scope='module')
def access_token_init():
    print('写入token值')
    get_access_token()
    yield
    print('结束')


@pytest.fixture(scope='module')
def member_init():
    print('初始化member实例')
    member = MemberManagement()
    yield member
    print('完成member实例')