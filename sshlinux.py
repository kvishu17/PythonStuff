import paramiko

ip = "192.168.1.78"
username = "groot"
password = "aditya"

remote_conn_pre=paramiko.SSHClient()
remote_conn_pre
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)
remote_conn = remote_conn_pre.invoke_shell()
remote_conn.send("cd /home/groot/Downloads\n")
remote_conn.send("mkdir Testpy\n")
remote_conn.send("cd /Testpy\n")
