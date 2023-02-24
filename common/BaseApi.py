# -*- coding:utf-8 -*-
import os
from configs import dir_path
import requests
from libs.login_token import read_access_token


class BaseApi:
    def __init__(self):
        file_name = os.path.join(dir_path.configs_path, 'access_token.yaml')
        self.access_token = read_access_token(file_name)
