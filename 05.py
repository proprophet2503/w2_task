isp_dataused = float(input("Enter the amount of data used in Gbs: "))

if(isp_dataused < 0.0):
    print("Bad data, please enter a valid data usage!")
else:

    if(isp_dataused > 0.0 and isp_dataused <= 1.0):
        charges = 250
    elif (isp_dataused <= 2.0):
        charges = 500
    elif (isp_dataused <= 5.0):
        charges = 1000
    elif (isp_dataused <= 10.0):
        charges = 1500
    elif (isp_dataused > 10.0):
        charges = 2000
    
    print(f"You are charged ${charges} for this month")



