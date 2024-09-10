def time_to_seconds(h, m, s):
    return h * 3600 + m * 60 + s

def seconds_to_hms(seconds):
    h = seconds // 3600
    seconds %= 3600
    m = seconds // 60
    s = seconds % 60
    return h, m, s

def main():
    # Input the event time (HH:MM:SS) in GMT+2
    event_time = input("Input the event time in GMT+2 with the format HH:MM:SS-->").strip()
    event_h, event_m, event_s = map(int, event_time.split(':'))

    # Input the current time (HH:MM:SS) in GMT+7
    current_time = input("Input the event time in GMT+7 with the format HH:MM:SS--> ").strip()
    current_h, current_m, current_s = map(int, current_time.split(':'))

    # Step 1: Adjust the event time from GMT+2 to GMT+7 by adding 5 hours
    event_h = (event_h + 5) % 24

    # Step 2: Convert both event time and current time into seconds
    event_seconds = time_to_seconds(event_h, event_m, event_s)
    current_seconds = time_to_seconds(current_h, current_m, current_s)

    # Step 3: Compute the difference in seconds
    if event_seconds < current_seconds:
        print("See you on the next Pear Event!")
    else:
        wait_seconds = event_seconds - current_seconds
        # Convert the difference back into H:M:S
        h, m, s = seconds_to_hms(wait_seconds)
        print(f"{h:02}:{m:02}:{s:02}")

main()
