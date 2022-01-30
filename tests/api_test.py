import json
import requests


def test_post_data():
    """
    Test the post_data function

    :return:
    """
    url = "http://localhost:8081"
    headers = {"ContentType": "application/json"}
    data = {"request": "test request"}
    data = json.dumps(data)
    response = requests.post(url, headers=headers, data=data)
    print("POST Response:")
    print(response)
    assert response.ok
