import datetime as dt
import smtplib
import pandas
import random
from pandas import *

# constants
MY_EMAIL = "email@gmail.com"
MY_PASSWORD = "your_password"

# 1. Update the birthdays.csv

data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
current_day = now.day
current_month = now.month

for item in data_dict:
    birthday = item["day"]
    birth_month = item["month"]
    name = item["name"]
    email = item["email"]
    if current_day == birthday and current_month == birth_month:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
        # actual name from birthdays.csv
        letter_number = random.randint(1, 3)
        file_path = f"letter_templates/letter_{letter_number}.txt"
        with open(file_path) as letter_template:
            contents = letter_template.read()
            contents = contents.replace("[NAME]", name)

        # 4. Send the letter generated in step 3 to that person's email address.

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_PASSWORD,
                to_addrs=email,
                msg=f"Subject:Happy Birthday {name}\n\n{contents}"
            )



