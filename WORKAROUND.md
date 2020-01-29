Triggers product/offer update

url = 'http://localhost:8000/api/auction/buffer/1/'
data = {'value': datetime.now()}
auth = (<superuser.credentials>)
requests.put(url=url, data=data, auth=auth)
