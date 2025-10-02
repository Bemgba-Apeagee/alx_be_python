from datetime import datetime, timedelta

def display_current_datetime():
    # Displays the current date and time in YYYY-MM-DD HH:MM:SS format
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)
    return current_date  # return for reuse


def calculate_future_date(days):
    # Calculates the future date after adding 'days' to the current date."""
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"The date after {days} days will be:", formatted_future_date)
    return future_date


# Run the script
if __name__ == "__main__":
    # Part 1: Display current date and time
    display_current_datetime()

    # Part 2: Ask user for days to add
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days_to_add)
    except ValueError:
        print("Please enter a valid integer for the number of days.")
