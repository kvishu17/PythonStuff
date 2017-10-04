#Some changes
#import ipcalc
#for x in ipcalc.Network('172.16.1.0/30'):
#    print str(x)

#Network = ipcalc.Network('172.16.1.0/30')
#172.16.1.1' in Network
import ipaddress
n1 = ipaddress.ip_network(u'172.16.1.0/28')
n2 = ipaddress.ip_network(u'172.16.1.1/32')
list(n1.address_exclude(n2))
