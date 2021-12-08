# API URL
import requests

url = "https://reqres.in/api/users?pages=2"


def get_users_detail(url):
  """
  get users data for each page
  """
  
  response = requests.get(url)
  return response.json()



# check if George and Emma are there in the response

result = get_users_detail(url)

names = ["George", "Emma"]
for i in result['data']:
  if i['first_name'] in names:
    print(f"{i['first_name']} is present in response")

