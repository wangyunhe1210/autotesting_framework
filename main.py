# from libs.login_token import Login
import os
from configs.dir_path import configs_path
from utils.yaml_handle import read_yaml
from libs.login_token import Login

# login = Login()
# res = login.get_access_token(os.path.join(configs_path, 'access_token.yaml'))


login = Login()
login.get_access_token(os.path.join(configs_path, 'access_token.yaml'))