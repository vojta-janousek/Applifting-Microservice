Triggers product/offer update

import requests

from datetime import datetime

url = 'http://localhost:8000/api/auction/buffer/1/'
data = {'value': datetime.now()}
auth = (<superuser.credentials>)
requests.put(url=url, data=data, auth=auth)

Buffer has to be set. Create a superuser, go to admin interface
and manually create a Buffer object. Then, use the superuser credentials
to send a put request (see above).
