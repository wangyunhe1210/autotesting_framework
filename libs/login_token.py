# -*- coding:utf-8 -*-
import os
import requests
import yaml

root_path = os.path.dirname(__file__)
name = os.path.join(root_path, 'access_token.yaml')

def get_access_token(company_id='ww9c395f7fc48d9866', secret='P4q05ResCx5qbGF8msryzamVi2K8yCvCDwBDEonqN7s'):
    payload = {'corpid': company_id, 'corpsecret': secret}
    res = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken', payload)
    return res.json()['access_token']


def write_yaml(file_name, datas):
    with open(file_name, 'w', encoding='utf8') as f:
        yaml.dump(datas, f)


def read_yaml(file_name):
    with open(file_name, 'r', encoding='utf8') as f:
        yaml.safe_load(f)


if __name__ == '__main__':
    data = {'token': get_access_token()}
    write_yaml(name, data)
