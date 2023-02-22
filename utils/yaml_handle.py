# -*- coding:utf-8 -*-

import yaml


def write_yaml(file_name, datas):
    """
    写入yaml文件
    :param file_name: yaml文件路径
    :param datas: 写入参数
    :return: 无
    """
    with open(file_name, 'w', encoding='utf8') as f:
        yaml.dump(datas, f)


def read_yaml(file_name):
    """
    读取yaml文件
    :param file_name: yaml文件路径
    :return: 读取结果
    """
    with open(file_name, 'r', encoding='utf8') as f:
        res = yaml.safe_load(f)
        return res


def update_yaml(file_name, datas: dict):
    """
    更新yaml文件
    :param file_name: yaml文件路径
    :param datas: 更新数据，以字典格式存放
    :return: 无
    """
    old_yaml = read_yaml(file_name)
    for i in datas:
        old_yaml[i] = datas[i]
    with open(file_name, 'w', encoding='utf8') as f:
        yaml.dump(old_yaml, f)
