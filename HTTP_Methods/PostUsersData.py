import requests
from requests.api import post

url = "https://reqres.in/api/users"

payload = {
    "name": "Ashish",
    "job": "Senior software Engineer"
}

def post_users_data(url, payload):

    response = requests.post(url, payload)
    assert response.status_code == 201
    result = response.json()

    # verify user response data is correct
    assert result['name'] == payload['name']
    assert result['job'] == payload['job']

    return "data persists successfully"



# verify user response data is correct
print(post_users_data(url, payload))

