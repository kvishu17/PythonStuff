import xlrd # Importing library for excel document manipulation
import os.path #Importing library to set path for excel document in OS
import ipaddress #Importing library for IP address manipulation
#Set the path of excel file stored in your computer and open the excel document
wb = xlrd.open_workbook(os.path.join('C:\Users\jeegnesh\Documents\Python_stuff','HSRP_MH.xlsx'))
wb.sheet_names()  #Gives names of all sheets in the excel
sh = wb.sheet_by_index(0)
n=0 #Rows start from zero
i=0 #Columns start from zero
#Function for Primary router HSRP configuration
#val=vlan_id, bsc=BSC_id, plane=CP_UP_plane, pop=pop_id, prim=IP address of primary, vir=Vortual IP address
def primary(val, bsc, plane, pop, vrf, prim, vir):
    x = """
Primary N3K
!
no interface Ethernet1/24.%s
interface Ethernet1/24.%s
  description %s_%s_Site_Fiber POP_%s
  encapsulation dot1q %s
  %s
  ip address %s/28
  hsrp version 2
  hsrp delay minimum 30 reload 60
  hsrp %s
   preempt
   priority 120
   timers msec 300 msec 900
   ip %s
  !
 !
!
""" % (val, val, bsc, plane, pop, val, vrf, prim, val, vir)
    return x

def secondary(val, bsc, plane, pop, vrf, secd, vir):
    y = """
Secondary N3K
!
no interface Ethernet1/24.%s
interface Ethernet1/24.%s
  description %s_%s_Site_Fiber POP_%s
  encapsulation dot1q %s
  %s
  ip address %s/28
  hsrp version 2
  hsrp delay minimum 30 reload 60
  hsrp %s
   preempt
   priority 90
   timers msec 300 msec 900
   ip %s
  !
 !
!
""" % (val, val, bsc, plane, pop, val, vrf, secd, val, vir)
    return y

for n in range(sh.nrows):
    vlan_id = "%d" % sh.cell_value(n,0) #fetching value of vlan_id
    BSC_id = "%s" % sh.cell_value(n,1) #fetching value of BSC ID
    pop_id = "%s" % sh.cell_value(n,3) #fetching value of pop id
    if pop_id.replace('.','',1).isdigit(): #If the pop_id value has digits with floating point,
    #then convert string to float and then to integer.
        pop_id = float(pop_id)
        pop_id = int(pop_id)
    else: #If pop_id value is string then value will remain same
        pop_id = "%s" % sh.cell_value(n,3)
    CP_UP_plane = "%s" % sh.cell_value(n,4) #Link description of CP or UP plane
    if CP_UP_plane == 'UP':
        vrf_name = 'vrf member P-Abis'
    elif CP_UP_plane == 'MP':
        vrf_name = '!'
    ipadd = "%s" % sh.cell_value(n,2) #Accessing IP network
    net4 = ipaddress.ip_network(u'%s' % ipadd, strict=False)
    sec = net4[-2]#Secondary/standby IP address
    pri = net4[-3]#Primary/Active Ip address
    virtual = net4[1]#Virtual IP address
    primary(vlan_id, BSC_id, CP_UP_plane, pop_id, vrf_name, pri, virtual)#Executing primary function definition
    secondary(vlan_id, BSC_id, CP_UP_plane, pop_id, vrf_name, sec, virtual)#Executing secondary function definition
    #Creating a text file to save the function output to a file
    text = open("%s_%s_hsrp_config.txt" % (BSC_id, vlan_id), 'w')
    text.write(primary(vlan_id, BSC_id, CP_UP_plane, pop_id, vrf_name, pri, virtual)) #Writing output of primary function to text file
    text.write(secondary(vlan_id, BSC_id, CP_UP_plane, pop_id, vrf_name, sec, virtual)) #Writing output of secondary function to text file
    text.close() #Closing text file
