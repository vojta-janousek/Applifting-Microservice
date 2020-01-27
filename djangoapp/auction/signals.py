import requests

from decouple import config


def register_product(sender, **kwargs):
    '''
    Gets triggered when a new product is created in the auction microservice.
    Registers said product in the Offers microservice.
    '''
    base_url = 'https://applifting-python-excercise-ms.herokuapp.com/api/v1'
    register_endpoint = '/products/register'
    register_url = base_url + register_endpoint

    token = config('ACCESS_TOKEN')
    headers = {
        'Bearer': token
    }

    # if kwargs['created']:
    #     product_data = {
    #         'id': kwargs['instance'].id,
    #         'name': kwargs['instance'].name,
    #         'description': kwargs['instance'].description
    #     }
    #
    #     register_request = requests.post(
    #         url = register_url,
    #         data=product_data,
    #         headers=headers
    #     )
    #     print(register_request.status_code)
