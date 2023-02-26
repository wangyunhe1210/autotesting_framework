# -*- coding:utf-8 -*-
import os
import requests
from utils import yaml_handle
from configs.dir_path import configs_path


def get_access_token(file_name=os.path.join(configs_path, 'access_token.yaml')):
    """
    获取登录token
    :param file_name: 存放登录信息的yaml文件
    :return: access_token
    """
    data = yaml_handle.read_yaml(file_name)
    company_id = data['login_info']['corpid']
    secret = data['login_info']['corpsecret']
    url = data['login_info']['host'] + data['login_info']['url']
    method = data['login_info']['method']
    payload = {'corpid': company_id, 'corpsecret': secret}
    res = requests.request(method, url, params=payload).json()
    token = {'token': res['access_token']}
    if 'token' in data:
        yaml_handle.update_yaml(file_name, token)
    else:
        yaml_handle.write_yaml(file_name, token)
