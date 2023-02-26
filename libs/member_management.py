# -*- coding:utf-8 -*-
from common.BaseApi import BaseApi
from configs import dir_path


class MemberManagement(BaseApi):
    def read_member(self):
        payload = {'access_token': self.access_token, 'userid': 'laozhang123'}
        resp = self.request_send(payload)
        return resp

