
wt_lb = float(input("Enter your weight in pounds :"))
ht_in= float(input("Enter your height in inches :"))

print(wt_lb, "   ", ht_in)

bmi = 703 * wt_lb/ (ht_in**2) 


if (bmi < 0):
    print("Enter a valid weight and height")
else:
    if(bmi < 18.5):
        print("Underweight")
    elif(bmi <= 24.9):
        print("Normal")
    elif(bmi <= 29.9):
        print("Overweight")
    else:
        print("Obese")




