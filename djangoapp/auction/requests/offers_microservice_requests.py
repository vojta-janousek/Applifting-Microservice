import requests
import json
import time

from decouple import config


# Token acquisition

base_url = 'https://applifting-python-excercise-ms.herokuapp.com/api/v1'
auth_endpoint = '/auth'
auth_url = base_url + auth_endpoint

# token_request = requests.post(url=auth_url)
# print(token_request.status_code) -> 200
# print(json.dumps(token_request.text)['access_token']) -> token

token = config('ACCESS_TOKEN')

# Register a product

product_data = {
    'id': 1,
    'name': 'Rybi kompot',
    'description': 'Snizuje delku zivota'
}
register_endpoint = '/products/register'
register_url = base_url + register_endpoint
headers = {
    'Bearer': token
}

# register_request = requests.post(
#                         url=register_url,
#                         data=product_data,
#                         headers=headers
#                         )

# Retrieve all offers for a single product

offers_url = base_url + '/products/1/offers'
# offer_request = requests.get(url=offers_url, headers=headers)

def compare_ids(url, headers):
    '''
    Calls two identical offers requests separated by a minute, then
    returns the number of mutual id numbers between them.
    '''
    first_request = requests.get(url=url, headers=headers)
    first_data = json.loads(first_request.text)

    time.sleep(70)

    second_request = requests.get(url=url, headers=headers)
    second_data = json.loads(second_request.text)

    count = 0
    for first_offer in first_data:
        first_id = first_offer['id']
        for second_offer in second_data:
            second_id = second_offer['id']
            if (first_id == second_id):
                count += 1

    return [count, len(first_data), len(second_data)]

if (__name__ == '__main__'):
    offer_url = offers_url
    headers = {
        'Bearer': token
    }
    res = compare_ids(offer_url, headers)
    print('Mutual: {}, First: {}, Second: {}'.format(res[0], res[1], res[2]))
