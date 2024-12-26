print("Here, \n You will calculate the your electricity bill")
print("Firstly, \n Enter the following information")

units = int(input("Enter your consumed unit in numbers "))
if units < 50:
    amount = units * 2.6
    tax = 25
elif units <= 100:
    amount = units * 3.25
    tax = 35
elif units <= 150:
    amount = units * 4.26
    tax = 55
elif units <= 200:
    amount = units * 5.23
    tax = 66
else:
    amount = units * 8.34
    tax = 75

total = amount + tax
print("Your electricity bill is ", total)