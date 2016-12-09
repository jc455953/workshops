__author__ = 'jc455953'
lower = 10
upper = 100
#print("enter a number(" + str(lower) + "-" + str(upper) + "/:")
str = "enter a number {} - {}:".format(lower,upper)
print(str)
for i in range(lower,upper):
    print(" AASCII{:3} CHAR{:<8}".format(i, chr(i)))





