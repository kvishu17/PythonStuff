def add(a,b):
    print "Adding %d + %d" % (a, b)
    return a + b

def subtract(a,b):
    print "Subtracting %d - %d" % (a, b)
    return a - b

def multiply(a,b):
    print "Multiplying %d * %d" % (a, b)
    return a * b

def division(a,b):
    print "dividing %d / %d" % (a, b)
    return a / b

age = add(30, 5) #How Old are you?
height = subtract(78, 4) #Height in Inches
weight = multiply(90,2)#Weight in Kgs
iq = division(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "Here is the puzzle"

what = add(age, subtract(height, multiply(weight, division(iq, 2))))

print "That becomes: ", what
