from netmiko import ConnectHandler
cisco_881 = {'device_type':'cisco_ios', 'ip':'192.168.10.1', 'username':'infadmin', 'password':'Select@987'}
net_connect = ConnectHandler(**cisco_881)
net_connect.find_prompt()
output1 = net_connect.send_command("show run | inc logging")
print(output1)
config_commands = ['logging buffered 19999']
output = net_connect.send_config_set(config_commands)
print(output)
output1 = net_connect.send_command("show run | inc logging")
print(output1)
