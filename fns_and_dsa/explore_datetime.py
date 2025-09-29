import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d : %H:%M:%S")
    print("Current date and time is: ", formatted_date)


from datetime import datetime, timedelta

def calculate_future_date(days: int):
    today = datetime.today()
    future_date = today + timedelta(days=days)
    formatted_date = future_date.strftime("%Y-%m-%d : %H:%M:%S")

    # Print the result
    print(f"Future date: {formatted_date}")


# Prompt user for input
days = int(input("Enter the number of days: "))
calculate_future_date(days)
