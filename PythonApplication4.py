from netmiko import ConnectHandler
from datetime import datetime
cisco_881 = {'device_type':'cisco_ios', 'ip':'192.168.10.1', 'username':'infadmin', 'password':'Select@987'}
net_connect = ConnectHandler(**cisco_881)
start_time = datetime.now()
output = net_connect.send_command("sh ip int br")
print ("\n\n***************Cisco IOS*****************")
print(output)
print("****************END******************")
end_time = datetime.now()
total_time = end_time - start_time
print(total_time)
