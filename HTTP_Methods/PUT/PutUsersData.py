from urllib import request


from requests.api import put

url = "https://reqres.in/api/users/2"
data = {
    "name": "morpheus",
    "job": "zion resident"
}

def update_entire_user_data(url, data):
    """
    updating entire user data needs two arguments
    Arguments : 
    url       : url which needs to be updated
    data      : data which needs to be put for the given resource
    """

    response = put(url, data)
    assert 200 == response.status_code


update_entire_user_data(url, data)

