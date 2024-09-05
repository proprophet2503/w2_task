purchase_total = float(input("Enter the purchase total: "))
student_check = input("Enter 1 if you are a student and 0 if you are not a student:")

tax = 0.05
discount = 0.2 

taxed_price = purchase_total * 0.05

if (student_check == "1"):
    students_discount = purchase_total * discount
    discounted_price = purchase_total - students_discount

    total = discounted_price + taxed_price

    print("Total purchases : $%.2f" %purchase_total)
    print("Student's discount (20%) : $%.2f" %students_discount)
    print("Discounted total : $%.2f" %discounted_price)
    print("Sales tax (5%) : $%.2f" %taxed_price)
    print("Total : $%.2f" %total)

else:
    total = purchase_total + taxed_price
    print("Total purchases : $%.2f" %round(purchase_total, 2))
    print("Sales tax (5%) : $%.2f" %round(taxed_price, 2))
    print("Total : $%.2f" %round(total, 2))