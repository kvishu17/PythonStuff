from sys import argv

scripts, ip_addr = argv
print "We are converting IP %s into binary format" % ip_addr
octets = ip_addr.split('.')
ip_addr_bin = []

if len(octets) == 4:
    for octet in octets:
        bin_octet = bin(int(octet))
        bin_octet = bin_octet[2:]
        while True:
            if len(bin_octet) >= 8:
                break
            bin_octet = '0' + bin_octet
        ip_addr_bin.append(bin_octet)

    ip_addr_bin = ".".join(ip_addr_bin)

    print "\n%-15s %-45s" % ("IP ADDRESS", "BINARY")
    print "\n%-15s %-45s" % (ip_addr, ip_addr_bin)
else:
    print "Invalid IP address"
