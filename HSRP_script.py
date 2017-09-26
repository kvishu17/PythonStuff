import xlrd

book = xlrd.open_workbook("hsrp_N3k.xlsx")

first_sheet = book.sheet_by_index(0)

data = [[first_sheet.cell_value(r,c) for c in range(first_sheet.ncols)] for r in range(first_sheet.nrows)]

x = data[0][1]

x = int(x)
x = x + 1

POP_ID = first_sheet.col_values(0)
BSC_ID = first_sheet.col_values(1)
CP_UP_VLAN = first_sheet.col_values(2)
CP_UP_gateway = first_sheet.col_values(3)
CP_UP_pri_IP = first_sheet.col_values(4)
CP_UP_sec_IP = first_sheet.col_values(5)
CP_UP_hsrp = first_sheet.col_values(6)
M_VLAN = first_sheet.col_values(7)
M_gateway = first_sheet.col_values(8)
M_pri_IP = first_sheet.col_values(9)
M_sec_IP = first_sheet.col_values(10)
M_hsrp = first_sheet.col_values(11)

counter = 2



while counter <= x:
    print "  description %s_UP_Site_Fiber POP_%s" % (BSC_ID[counter], POP_ID[counter])
    counter = counter + 1
