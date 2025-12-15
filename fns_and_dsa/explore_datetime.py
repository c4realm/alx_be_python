from datetime import datetime, timedelta

#display the date 

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    print("Current date and time:", formatted_date)
#calculate a future date

def calculate_future_date():
    days = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.now()
    future_date = current_date + timedelta(days = days)
    print("Future date: ", future_date.strftime("%Y-%m-%d"))

display_current_datetime()
calculate_future_date()

