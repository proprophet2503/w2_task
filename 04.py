cylinders_color = input("Enter the first letter of the color of the observed gas cylinder: ('Y' or 'y' for Yellow) : ").upper()

match cylinders_color:
    case 'O':
        print("Ammonia")
    case 'B':
        print("Carbon Monoxide")
    case 'Y':
        print("Hydrogen")
    case 'G':
        print("Oxygen")
    case _:
        print("Enter a valid input!")