import math

# Constants
BASE_RATE = 3999  # $39.99 stored as cents
WEEKDAY_LIMIT = 600  # 600 weekday minutes included in base rate
EXTRA_MINUTE_COST = 40  # $0.40 per additional weekday minute, stored as cents
TAX_RATE = 5.25 / 100  # 5.25% tax

# Input from the user
weekday_minutes = int(input("Enter the number of weekday minutes used: "))
night_minutes = int(input("Enter the number of night minutes used: "))
weekend_minutes = int(input("Enter the number of weekend minutes used: "))

# Calculate the extra weekday minutes and cost
if weekday_minutes > WEEKDAY_LIMIT:
    extra_weekday_minutes = weekday_minutes - WEEKDAY_LIMIT
    extra_weekday_cost = extra_weekday_minutes * EXTRA_MINUTE_COST
else:
    extra_weekday_minutes = 0
    extra_weekday_cost = 0

# Calculate the pretax bill in cents
pretax_bill = BASE_RATE + extra_weekday_cost

# Calculate the taxes in cents (rounded)
taxes = math.ceil(pretax_bill * TAX_RATE)

# Calculate the total bill in cents
total_bill = pretax_bill + taxes

# Calculate the total minutes (weekday, night, and weekend)
total_minutes = weekday_minutes + night_minutes + weekend_minutes

# Calculate the average minute cost before taxes (rounded to the nearest cent)
if total_minutes > 0:
    avg_minute_cost = math.ceil(pretax_bill / total_minutes)
else:
    avg_minute_cost = 0  # If no minutes are used

# Display results
print("\n--- Monthly Bill Breakdown ---")
print(f"Weekday minutes used: {weekday_minutes}")
print(f"Night minutes used: {night_minutes}")
print(f"Weekend minutes used: {weekend_minutes}")
print(f"Pretax bill: ${pretax_bill / 100:.2f}")
print(f"Average minute cost (before taxes): ${avg_minute_cost / 100:.2f}")
print(f"Taxes: ${taxes / 100:.2f}")
print(f"Total bill: ${total_bill / 100:.2f}")
