from unittest.mock import patch
from requests.api import patch


url = "https://reqres.in/api/users/2"
data = {
    "name": "morpheus",
    "job": "zion resident"
}

def update_user_data(url, data):
    """
    will update the user data using patch
    verb
    Arguments:
    url      :  url which needs to be updated
    data.    :  records which needs to be updated 
                for the given user
    """

    response = patch(url, data)

    # verify the response code, should return 200
    # for successful patch
    assert 200 == response.status_code


update_user_data(url, data)