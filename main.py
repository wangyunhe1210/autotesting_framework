# from libs.login_token import Login
import os
from configs.dir_path import configs_path
from utils.yaml_handle import read_yaml
import requests
import json

# login = Login()
# res = login.get_access_token(os.path.join(configs_path, 'access_token.yaml'))


# url = 'http://127.0.0.1:5000/post_method_one'
# payload = {'first': 2, 'second': 3}
# headers = {"Content-Type": "application/json"}
# res = requests.post(url, data=json.dumps(payload), headers=headers).json()
# print(res)


# url = 'http://127.0.0.1:5000/post_method_two'
# payload = {'first': 2, 'second': 3}
# headers = {"Content-Type": "application/x-www-form-urlencoded"}
# res = requests.post(url, data=payload, headers=headers).json()
# print(res)