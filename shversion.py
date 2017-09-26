cisco_ios = raw_input("enter the first line of show version:")

ios = cisco_ios.split(',')
version = ios[2]
print version
ios_version = version[9:]
print ios_version
