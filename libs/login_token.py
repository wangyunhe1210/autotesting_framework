# -*- coding:utf-8 -*-
import os
import requests
from utils import yaml_handle
from configs import dir_path

name = os.path.join(dir_path.configs_path, 'access_token.yaml')


def get_access_token(file_name):
    """
    获取登录token
    :param file_name: 存放登录信息的yaml文件
    :return: access_token
    """
    company_id = yaml_handle.read_yaml(file_name)['login_info']['corpid']
    secret = yaml_handle.read_yaml(file_name)['login_info']['corpsecret']
    payload = {'corpid': company_id, 'corpsecret': secret}
    res = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken', payload)
    return res.json()['access_token']


def write_access_token(file_name):
    """
    写入登录token
    :param file_name: 存放登录信息的yaml文件
    :return: 无
    """
    data = {'token': get_access_token(file_name)}
    yaml_handle.write_yaml(file_name, data)


def update_access_token(file_name):
    """
    更新登录token
    :param file_name: 存放登录信息的yaml文件
    :return: 无
    """
    data = {'token': get_access_token(file_name)}
    yaml_handle.update_yaml(file_name, data)


def read_access_token(file_name):
    """
    读取登录token
    :param file_name: 存放登录信息的yaml文件
    :return: access_token
    """
    access_token = yaml_handle.read_yaml(file_name)['token']
    return access_token


if __name__ == '__main__':
    print(read_access_token(name))