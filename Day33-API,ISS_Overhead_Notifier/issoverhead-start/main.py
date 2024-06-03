import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 55.751244 # Your latitude
MY_LONG = 37.618423 # Your longitude

USERNAME = "andrewch2817@gmail.com"
PASSWORD = "jpht vykj zqtm ungw"

#Checking distance from ISS to myself
def check_distance():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 < iss_latitude < MY_LAT+5 and MY_LONG-5 < iss_longitude < MY_LONG+5:
        return True

#Checking for the night to come
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

#If the ISS is close to my current position and it is currently dark
#Sending the letter
while True:
    time.sleep(60)
    if check_distance():
        if int(sunset) <= time_now or int(sunrise) >= time_now:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=USERNAME, password=PASSWORD)
                connection.sendmail(
                    from_addr=USERNAME,
                    to_addrs=USERNAME,
                    msg=f"Subject: Look up!\n\nISS is above you in the sky :)"
                )
# BONUS: run the code every 60 seconds.



