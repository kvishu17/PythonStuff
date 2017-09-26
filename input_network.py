ip_network = raw_input("\n Enter the valid IP network:")

octets = ip_network.split('.')
octets = octets[:3]
print octets
octets.append('0')

network_number = ".".join(octets)
print network_number

first_octet_bin = bin(int(octets[0]))
first_octet_hex = hex(int(octets[0]))

print "%10s %10s %10s" % ("NETWORK_NUMBER", "FIRST_OCTET_BINARY", "FIRST_OCTET_HEX")
print "%10s %12s %15s" % (network_number, first_octet_bin, first_octet_hex)

first_octet_bin = bin(int(octets[0]))
second_octet_bin = bin(int(octets[1]))
third_octet_bin = bin(int(octets[2]))
fourth_octet_bin = bin(int(octets[3]))

print "%20s %20s %20s %20s" % ('fist_octet', 'second_octet', 'third_octet', 'fourth_octet')
print "%20s %20s %20s %20s" % (first_octet_bin, second_octet_bin, third_octet_bin, fourth_octet_bin)
