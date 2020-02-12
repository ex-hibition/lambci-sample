import requests
import paramiko
import json


def lambda_handler(event, context):
    """
    ハンドラメソッド
    """
    get_ssh_exec_ls()

    return json.dumps({"result": "ok"})


def get_ssh_exec_ls():
    """
    sshしてls結果を取得する
    """
    with paramiko.SSHClient() as ssh:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname='172.17.0.2', port=14022,
                    username='testuser', key_filename='id_rsa.pem')

        # コマンド実行
        stdin, stdout, stderr = ssh.exec_command("cd / && ls -1 | awk '{print $0}'")

        # 対象ファイル存在チェック
        filterd_list = [x.rstrip('\n') for x in stdout if x.startswith('m')]

        # 複数存在チェック
        if len(filterd_list) > 1:
            print(f"条件にヒットするファイルが複数ファイル存在します:{filterd_list}")
