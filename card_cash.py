
# customer pay terminal
print("Method of payment - Cash = 1 or Card = 2")
# customer payment choice
payment_choice = float(input("Enter your Choice of Payment: "))
if payment_choice == 1 or payment_choice == 2:
    pass
else:
    print("Invalid Entry")
if payment_choice == 1:
    print("You chose Cash")
    pass
elif payment_choice == 2:
    print("You chose Card")
    pass

