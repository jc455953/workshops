__author__ = 'jc455953'

#Program to calculate and display a user's bonus based on sales.
#If sales are under $1,000, the user gets a 10% bonus.
#If sales are $1,000 or over, the bonus is 15%.
sale = float(input("enter sales:"))
if sale <= 1000:
    bonus = 10/100 * sale
    print("bonus is ",bonus)
elif sale >= 1000:
    bonus = 15/100 * sale
    print("bonus is",bonus )
