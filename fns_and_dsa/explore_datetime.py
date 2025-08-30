#!/usr/bin/env python3
from datetime import datetime, timedelta

def display_current_datetime():
    # save the current date inside a variable
    current_date = datetime.now()
    # format the date as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(days):
    # save the future date inside a variable
    future_date = datetime.now() + timedelta(days=days)
    # format the date as "YYYY-MM-DD"
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")
    return future_date

if __name__ == "__main__":
    # Part 1
    display_current_datetime()

    # Part 2
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days_to_add)
    except ValueError:
        print("Please enter a valid integer.")
