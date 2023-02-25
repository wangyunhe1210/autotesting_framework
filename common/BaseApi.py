# -*- coding:utf-8 -*-
import os
from configs import dir_path
import requests
from libs.login_token import read_access_token
from utils.yaml_handle import read_yaml
import inspect
from configs.config import HOST


class BaseApi:
    def __init__(self):
        file_name = os.path.join(dir_path.configs_path, 'access_token.yaml')
        self.access_token = read_access_token(file_name)
        self.data = read_yaml(os.path.join(dir_path.configs_path, 'apiConfig.yaml'))[self.__class__.__name__]

    def request_send(self, inData):
        try:
            func_name = inspect.stack()[1][3]
            data = self.data[func_name]
            print(HOST+data['url'])
            print(data['method'])
            resp = requests.request(method=data['method'], url=f'{HOST}'+data['url'], params=inData)
            return resp.json()
        except Exception as error:
            raise error
