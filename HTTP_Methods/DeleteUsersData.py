import requests

url = "https://reqres.in/api/users/2"

def delete_user(url):

    response = requests.delete(url)

    assert response.status_code == 204

    return "resource deleted successfully"


print(delete_user(url))
