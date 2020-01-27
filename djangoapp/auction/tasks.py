from __future__ import absolute_import, unicode_literals

import requests
import json

from celery import shared_task


@shared_task(name='summary')
def send_import_summary():
    auth = ('goulash.elemer@email.com', 'goulashelemer')
    data = {
        'name': 'Frozen yoghurt',
        'description': 'A cold snack'
    }
    url = 'http://localhost:8000/api/auction/product/'

    create_request = requests.post(url=url, data=data, auth=auth)
    print('yo')
