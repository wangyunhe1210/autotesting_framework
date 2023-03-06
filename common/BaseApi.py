# -*- coding:utf-8 -*-
import os
from configs import dir_path
import requests
from utils.yaml_handle import read_yaml
import inspect
from configs.config import HOST
import traceback
from utils.logging_handle import log


class BaseApi:
    def __init__(self):
        file_name = os.path.join(dir_path.configs_path, 'access_token.yaml')
        self.access_token = read_yaml(file_name)['token']
        self.data = read_yaml(os.path.join(dir_path.configs_path, 'apiConfig.yaml'))[self.__class__.__name__]

    def request_send(self, inData):
        try:
            func_name = inspect.stack()[1][3]
            data = self.data[func_name]
            resp = requests.request(method=data['method'], url=f'{HOST}' + data['url'], params=inData)
            return resp.json()
        except Exception as error:
            log.error(traceback.format_exc())
            raise error

    def query(self, inData):
        resp = self.request_send(inData)
        return resp

    def update(self, inData):
        resp = self.request_send(inData)
        return resp

    def add(self, inData):
        resp = self.request_send(inData)
        return resp

    def delete(self, inData):
        resp = self.request_send(inData)
        return resp


class BaseAssert:
    def define_assert(self, res, exData):
        try:
            assert res == exData
        except Exception as error:
            log.error(traceback.format_exc())
            raise error
