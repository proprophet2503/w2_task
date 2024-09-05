'''
The year can be evenly divided by 4, is a leap year, unless:

The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.

'''

def leap(year):
    if (year % 4 == 0):
        if(year % 100 == 0):
            if(year % 400 == 0):
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0;

def day_number(day, month, year):
    # Days in each month 
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Add one day to February for leap years
    if leap(year):
        days_in_month[1] = 29

    # Calculate the day number by summing up the days in previous months

    day_num = sum(days_in_month[:month - 1]) + day
    return day_num


# Example usage
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

print(f"The day number for {month}/{day}/{year} is: {day_number(day, month, year)}")