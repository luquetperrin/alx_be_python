from datetime import datetime, timedelta

def display_current_datetime():
  """Display the current date and time in YYYY-MM-DD HH:MM:SS format."""
  current_date = datetime.now()
  print("Current date and time:", current_date.strftime("%y-%m-%d %H:%M:%S"))

def calculate_future_date():
  """Prompt user for days to add and print the future date in YYYY-MM-DD format."""
  days_to_add = int(input("Enter the number of days to add to the current date: "))
  try:
    future_date = datetime.now() + timedelta(days=days_to_add)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
  except ValueError:
    print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()