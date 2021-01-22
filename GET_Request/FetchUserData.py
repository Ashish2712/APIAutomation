# API URL
import requests

url = "https://reqres.in//api/users?page=2"


def post(url):
  """
  post data on the url
  """
  data = {name: 'github'}
  
  response = requests.post(url, data)
  return response.status_code

