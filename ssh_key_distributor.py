# -*- coding: utf-8 -*-

from fabric.api import env, run, put, task
import getpass


env.hosts = ['your_host']  # 定義目標主機
env.user = 'your_user_name'      # 定義用戶名

@task
def distribute_key():
    local_pub_key_path = '/path/to/your/public/key.pub'  # 本地公鑰文件路徑
    remote_pub_key_path = '/tmp/pubkey.pub'              # 遠程臨時公鑰文件路徑
    put(local_pub_key_path, remote_pub_key_path)         # 上傳公鑰文件
    run('mkdir -p ~/.ssh && cat {} >> ~/.ssh/authorized_keys && rm {}'.format(remote_pub_key_path, remote_pub_key_path))  # 添加公鑰到授權鑰匙並清理
