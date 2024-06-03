import smtplib
import datetime
import random

my_email = "andrewch2817@gmail.com"
password = "jpht vykj zqtm ungw"

with open("quotes.txt") as file:
    quotes = file.readlines()

message = random.choice(quotes)

now = datetime.datetime.now()
if now.weekday() == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  #secured connection
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="katyak5670@gmail.com",
                            msg=f"Subject:Motivation\n\n{message}")
