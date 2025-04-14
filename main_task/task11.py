# Write a program that takes the date of birth of a person and the program outputs the age in terms of years,months,days TODAY.

# todays_date=('4-13-2025')
# birthdate=(input('Enter your birthdate mm/dd/yyyy: '))
# age=todays_date-birthdate
# print(age)


# from datetime import datetime
# from dateutil.relativedelta import relativedelta

# # Input: Date of Birth in YYYY-MM-DD format
# dob_input = input("Enter your date of birth (YYYY-MM-DD): ")

# try:
#     dob = datetime.strptime(dob_input, "%Y-%m-%d").date()
#     today = datetime.today().date()

#     if dob > today:
#         print("Date of birth cannot be in the future.")
#     else:
#         age = relativedelta(today, dob)
#         print(f"You are {age.years} years, {age.months} months, and {age.days} days old.")
# except ValueError:
#     print("Invalid date format. Please use YYYY-MM-DD.")


from datetime import date

def calculate_age(birth_date):
    today = date.today()

    # Initial difference
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    # Adjust if birthday hasn't occurred this month yet
    if days < 0:
        months -= 1
        # Get the number of days in the previous month
        last_month = today.month - 1 or 12
        last_month_year = today.year if today.month != 1 else today.year - 1
        days_in_prev_month = (date(last_month_year, last_month % 12 + 1, 1) - date(last_month_year, last_month, 1)).days
        days += days_in_prev_month

    if months < 0:
        years -= 1
        months += 12

    return years, months, days

# Input
dob_input = input("Enter your date of birth (YYYY-MM-DD): ")

try:
    birth_date = date.fromisoformat(dob_input)
    if birth_date > date.today():
        print("Date of birth cannot be in the future.")
    else:
        years, months, days = calculate_age(birth_date)
        print(f"You are {years} years, {months} months, and {days} days old.")
except ValueError:
    print("Invalid date format. Please use YYYY-MM-DD.")

