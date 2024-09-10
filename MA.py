# Function to determine the traffic light state
def traffic_light(M, N, T):
    
    # Total cycle: 85 seconds
    cycle_time = 85

    # Remaining time in the current cycle
    time_in_cycle = T % cycle_time

    # Determine how many cars can pass based on green light time
    if 25 <= time_in_cycle <= 85:
        # Green light is between 25 and 85 seconds (inclusive)
        green_light_time = time_in_cycle - 25  # Time after green light starts
        cars_that_can_pass = green_light_time // 5
    else:
        # If the light is red or yellow, no cars can pass
        cars_that_can_pass = 0

    # Total cars ahead of you
    total_cars_ahead = M + N
    
    # Cars left behind after some pass
    cars_left_behind = max(0, total_cars_ahead - cars_that_can_pass)

    # Determine if you can pass or not
    if M <= cars_that_can_pass:
        print("YES!", cars_left_behind)
    else:
        print("NO!", cars_left_behind)

# Example input (M, N, T)
M, N, T = map(int, input().split())

# Call the function with the input values
traffic_light(M, N, T)
