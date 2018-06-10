import requests
import json

TEMPLATE = "https://api.vk.com/method/{method_name}?{parameters}&access_token={access_token}&v=5.78"

def subscribe_to_group(group_id, access_token):
    parameters = 'group_id=' + group_id
    rec = requests.get(TEMPLATE.format(method_name = 'groups.join',
                                       parameters = parameters, access_token=access_token))

    response = rec.json()
    if response['response'] == 1:
        return True
    return response
