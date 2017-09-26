import openpyxl
import ipaddress
import xlrd
import os.path

#wb = xlrd.open_workbook(os.path.join('C:\Users\jeegnesh\Documents\Python_stuff','HSRP.xlsx'))
#wb.sheet_names()
#sh = wb.sheet_by_index(0)

#n=0
#i=0

excl = openpyxl.load_workbook('HSRP.xlsx')

sheet = excl.get_sheet_by_name('Sheet1')
def primary(val, bsc, pop, prim, vir):
    x = """
interface Ethernet1/24.%s
  description %s_UP_Site_Fiber POP_%s
  encapsulation dot1q %s
  vrf member P-Abis
  ip address %s/28
  hsrp %s
   preempt
   priority 120
   timers msec 300 msec 900
   ip %s
""" % (val, bsc, pop, val, prim, val, vir)
    return x

def secondary(val, bsc, pop, secd, vir):
    y = """
interface Ethernet1/24.%s
  description %s_UP_Site_Fiber POP_%s
  encapsulation dot1q %s
  vrf member P-Abis
  ip address %s/28
  hsrp %s
   preempt
   priority 90
   timers msec 300 msec 900
   ip %s
""" % (val, bsc, pop, val, secd, val, vir)
    return y


vlan_id = str(sheet['A2'].value)
BSC_id = str(sheet['B2'].value)
pop_id = str(sheet['D2'].value)
ipadd = str(sheet['C2'].value)
net4 = ipaddress.ip_network(u'%s' % ipadd, strict=False)
sec = net4[-2]
pri = net4[-3]
virtual = net4[-4]

#primary(vlan_id, BSC_id, pop_id, pri, virtual)
#secondary(vlan_id, BSC_id, pop_id, sec, virtual)

primary(vlan_id, BSC_id, pop_id, pri, virtual)
secondary(vlan_id, BSC_id, pop_id, sec, virtual)

#file=open("Output.txt","w")
#for n in range(sh.nrows):
#    data = "%s" % sh.cell_value(n,0)+" "
#    print data,
#    file.write(data+" ")
#    print
#    file.write("\n")
text = open("%s_hsrp_config.txt" % BSC_id, 'w')
text.write(primary(vlan_id, BSC_id, pop_id, pri, virtual))
text.write(secondary(vlan_id, BSC_id, pop_id, sec, virtual))
text.close()
