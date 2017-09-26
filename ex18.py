#This is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r and arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
    print "arg1: %r and arg2: %r" % (arg1, arg2)

def print_one(arg1):
    print "arg1: %r" % arg1

def print_none():
    print "I got nothing."

print_two("Vishwa", "The Great")
print_two_again("Vishwa", "The Great")
print_one("Vishwa, the Great!")
print_none()
