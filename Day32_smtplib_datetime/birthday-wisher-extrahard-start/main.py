##################### Extra Hard Starting Project ######################
import smtplib
import datetime
import pandas as pd
import random

USERNAME = "andrewch2817@gmail.com"
PASSWORD = "jpht vykj zqtm ungw"

#Pandas
df = pd.read_csv("birthdays.csv")
birthdays = {(row.month, row.day):row for index, row in df.iterrows()}

#datetime
today = datetime.datetime.now()
current_day = (today.month, today.day)

if current_day in birthdays:
    letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    letter = random.choice(letters)

    with open(f"letter_templates/{letter}") as file:
        text = file.read()
        text = text.replace("[NAME]", birthdays[current_day]["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
         connection.starttls()
         connection.login(user=USERNAME, password=PASSWORD)
         connection.sendmail(from_addr=USERNAME, to_addrs=USERNAME,
                             msg=f"Subject: Happy birthday!\n\n{text}")