__author__ = 'jc455953'

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator==0:
        print("denominator can be 0. try again..")
        denominator = int(input("enter the denominator:"))
        fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

print("Finished.")
