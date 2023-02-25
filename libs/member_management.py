# -*- coding:utf-8 -*-
from common.BaseApi import BaseApi
from libs.login_token import read_access_token
from configs import dir_path


class MemberManagement(BaseApi):
    def read_member(self):
        payload = {'access_token': self.access_token, 'userid': 'laozhang123'}
        resp = self.request_send(payload)
        print(resp)


if __name__ == '__main__':
    c = MemberManagement()
    c.read_member()
