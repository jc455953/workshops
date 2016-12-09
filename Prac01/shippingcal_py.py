__author__ = 'jc455953'
instruction = "welcome to our programme// number of items"
print(instruction)
noofitem = 1
while noofitem > 0:
    numofitem = int(input("pleaseinput the number of items:"))
    costperitem = float(input("the shipping cost for each item: $"))

    totalshipcost = numofitem * costperitem
    if totalshipcost > 100:
        totalshipcost = totalshipcost - (0.1 * totalshipcost)

    print("total cost of delivering your product is:",totalshipcost)