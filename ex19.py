def modak_and_laddus(modak_count, laddus_count):
    print "I have %d modak! :)" % modak_count
    print "I have %d laddus! :)" % laddus_count
    print "Ganpati Bappa Moraya!!\n"

print "We can give functions numbers directly:"
modak_and_laddus(21, 21)

print "OR, we can use variables from our script:"
modaks = 20
laddu = 30

modak_and_laddus(modaks, laddu)

print "We can do maths inside too:"
modak_and_laddus(10 + 20, 20 + 30)

print "And we can combine both, Variables and math:"
modak_and_laddus(modaks + 10, laddu + 20)
