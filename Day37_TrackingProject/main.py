import requests
from datetime import datetime

TOKEN =
USERNAME =
pixela_endpoint = "https://pixe.la/v1/users"

params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

## Step 1 - Here we have created a new user - we do not need to run it anymore
# response = requests.post(url=pixela_endpoint, json=params)
# print(response.text)


## Step 2 - creating a graph
GRAPH_ID =

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding",
    "unit": "Hour",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

## Step 3

#replace a-know with a username and test-graph with graph's id and add .html in the end
#https://pixe.la/v1/users/a-know/graphs/test-graph




## Step 4 - Posting a value to the graph
post_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()

post_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "3.00",
}

# response = requests.post(url=post_endpoint, json=post_params, headers=headers)
# print(response.text)

## Step5 - Updating values
put_endpoint = f"{post_endpoint}/{today.strftime("%Y%m%d")}"


put_params = {
    "quantity": "1.00"
}

# response = requests.put(url=put_endpoint, json=put_params, headers=headers)
# print(response.text)


## Step 6 - Deleting pixel

delete_endpoint = put_endpoint

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)