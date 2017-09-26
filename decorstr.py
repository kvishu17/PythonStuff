x = '4521.0'
if x.replace('.','').isdigit():
        x = float(x)
        x = int(x)
        print x
else:
    print x
