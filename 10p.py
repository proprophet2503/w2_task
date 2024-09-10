# Define time settings for each operation (in minutes)
bread_times = {
    "W": {  # White bread
        "primary_kneading": 15,
        "primary_rising": 60,
        "secondary_kneading": 18,
        "secondary_rising": 20,
        "loaf_shaping": 0.033,  # 2 seconds = 0.033 minutes
        "final_rising": 75,
        "baking": 45,
        "cooling": 30
    },
    "S": {  # Sweet bread
        "primary_kneading": 20,
        "primary_rising": 60,
        "secondary_kneading": 33,
        "secondary_rising": 30,
        "loaf_shaping": 0.033,  # 2 seconds = 0.033 minutes
        "final_rising": 75,
        "baking": 35,
        "cooling": 30
    }
}

# Function to display instructions for each step
def display_step(operation, time, is_double, is_manual):
    if is_double:
        time *= 1.5  # Increase time by 50% for double loaf
    time = round(time, 2)  # Round the time to 2 decimal places
    if operation == "loaf_shaping" and is_manual:
        print(f"{operation.replace('_', ' ').title()}: {time * 60:.0f} seconds")
    else:
        print(f"{operation.replace('_', ' ').title()}: {time} minutes")

# Function to compute and display bread making steps
def bread_machine(bread_type, is_double, is_manual):
    times = bread_times[bread_type]
    
    print("\n--- Bread Machine Process ---")
    display_step("primary_kneading", times["primary_kneading"], is_double, is_manual)
    display_step("primary_rising", times["primary_rising"], is_double, is_manual)
    display_step("secondary_kneading", times["secondary_kneading"], is_double, is_manual)
    display_step("secondary_rising", times["secondary_rising"], is_double, is_manual)
    display_step("loaf_shaping", times["loaf_shaping"], is_double, is_manual)

    if is_manual:
        print("Manual baking. Please remove the dough for further manual baking.")
    else:
        display_step("final_rising", times["final_rising"], is_double, is_manual)
        display_step("baking", times["baking"], is_double, is_manual)
        display_step("cooling", times["cooling"], is_double, is_manual)

# Main program



bread_type = input("Enter bread type (W for White, S for Sweet): ").strip().upper()
while bread_type not in ['W', 'S']:
    bread_type = input("Invalid choice. Please enter W for White or S for Sweet: ").strip().upper()

is_double = input("Is the loaf size double? (Y/N): ").strip().upper() == 'Y'
is_manual = input("Is the baking manual? (Y/N): ").strip().upper() == 'Y'

bread_machine(bread_type, is_double, is_manual)
