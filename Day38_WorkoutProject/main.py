import requests
from datetime import datetime
import os

API_KEY = ""
API_ID = ""
ENDPOINT = ""
SHEETY_API = ""

GENDER = "male"
WEIGHT_KG = "70"
HEIGHT_CM = "187"
AGE = "20"

text = input("Tell me which exercises you did?")

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

params = {
    "query": text,
    "gender": GENDER,
    "age": AGE,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
}

response = requests.post(url=ENDPOINT, json=params, headers=headers)
response.raise_for_status()

data = response.json()
print(data)



day = datetime.now().strftime("%Y/%m/%d")
time = datetime.now().strftime("%H:%M:%S")

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": day,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

response = requests.post(url=SHEETY_API, json=sheet_inputs)
response.raise_for_status()
print(response.text)
