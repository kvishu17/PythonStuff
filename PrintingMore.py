formatter =  "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("One", "Two", "Three", "Four")
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said GOOD NOGHT",
    )

print "I am 6'2\" tall."
print 'I am 6\'2" tall.'

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm a split \non a line."
baackslash_cat = "I'm \\ a \\ Cat."

fat_cat = """
I'll do a list:
\t* Cat Food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print baackslash_cat
print fat_cat

age = raw_input ("Age? ")
height = raw_input ("Height? ")
weight = raw_input ("Weight? ")
print "So you are %r years old, %r tall and %r heavy" % (age, height, weight)
