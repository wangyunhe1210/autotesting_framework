# -*- coding:utf-8 -*-
import os
import requests
from utils import yaml_handle

root_path = os.path.dirname(__file__)
name = os.path.join(root_path, 'access_token.yaml')


def get_access_token(file_name):
    company_id = yaml_handle.read_yaml(file_name)['login_info']['corpid']
    secret = yaml_handle.read_yaml(file_name)['login_info']['corpsecret']
    payload = {'corpid': company_id, 'corpsecret': secret}
    res = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken', payload)
    return res.json()['access_token']


def write_access_token(file_name):
    data = {'token': get_access_token(file_name)}
    yaml_handle.write_yaml(file_name, data)


def update_access_token(file_name):
    data = {'token': get_access_token(file_name)}
    yaml_handle.update_yaml(file_name, data)


def read_access_token(file_name):
    access_token = yaml_handle.read_yaml(file_name)['token']
    return access_token


if __name__ == '__main__':
    update_access_token(name)
