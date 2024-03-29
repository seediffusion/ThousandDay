from datetime import date, timedelta
from math import ceil
from pyperclip import copy
import msvcrt
import sys
def ThousandDay():
    date_str = input("Enter your birthday in the format year-month-day. For example, 2005-01-01\n")
    try:
        if date_str.startswith("[c]"):
            birthday = date.fromisoformat(date_str[3:])
        else:
            birthday = date.fromisoformat(date_str)
    except ValueError:
        print("Something went wrong with the date you entered. Please try again.")
        ThousandDay()
    current_date = date.today()
    days_passed = (current_date - birthday).days
    next_thousand = ceil(days_passed / 1000) * 1000
    if next_thousand == days_passed:
        print("Congratulations! Today, " + current_date.strftime("%A, %d %B, %Y") + ", is your " + str(next_thousand // 1000) + "th thousand day! This means you are precisely " + str(next_thousand) + " days old today!")
        if date_str.startswith("[3]"):
            copy("Congratulations! Today, " + current_date.strftime("%A, %d %B, %Y") + ", is your " + str(next_thousand // 1000) + "th thousand day! This means you are precisely " + str(next_thousand) + " days old today!")
    else:
        days_until = next_thousand - days_passed
        days_to_add = timedelta(days = days_until)
        new_date = (current_date + days_to_add).strftime("%A, %d %B, %Y")
        print("You are currently " + str(days_passed) + " days old. Your next thousand day will be on " + str(new_date) + ". There are " + str(days_until) + " days until your next thousand day!")
        if date_str.startswith("[c]"):
            copy("You are currently " + str(days_passed) + " days old. Your next thousand day will be on " + str(new_date) + ". There are " + str(days_until) + " days until your next thousand day!")
    waiting = True
    while waiting:
        print("Would you like to calculate another thousand day? Press Y or N.\n")
        retry = msvcrt.getch()
        if retry.lower() == b"y":
            waiting = False
            ThousandDay()
        elif retry.lower() == b"n":
            waiting = False
            sys.exit()
        else:
            print("You pressed an invalid key.")
if __name__ == "__main__":
    ThousandDay()