def within_x_percent(ref, data, x):

    substance_identified  = False
    for key in ref:
        if(data <= ref[key] + x * ref[key] and data >= ref[key] - x * ref[key]):

            substance_identified = True
            return "The substance that's being observed is:", key
            
        else:
            substance_identified  = False

    if (substance_identified == False):
        return "Invalid substance."        
        

def main():

    percent_x = float(input("Input the percantage of the tolerance: "))/100
    data_boiling = float(input("Enter the boiling point of the substance in Celcius: "))

    substance = {
        "Water": 100,
        "Mercury": 357,
        "Copper": 1187,
        "Silver": 2103,
        "Gold": 2660,
    
    }
    
    

    result = within_x_percent(substance, data_boiling, percent_x )
    print(result)

main()



