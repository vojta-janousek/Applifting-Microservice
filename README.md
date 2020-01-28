# Applifting-Microservice

IMPORTANT:

- To use the service, first create an account via an endpoint (see the list
  of endpoints below) or browseable API, then log in.
  You can list all your products, view a detail of a single product,
  or create a new product. Creating a new product will register it
  with the Offers microservice, and refresh its offers every minute.

  You cannot view any data created/registered by other users.

- Environment variables are hidden and ignored by git
- Application integrates Django, PostgreSQL, Celery and Redis via Docker
- You can use the following command to run unit tests on chosen <app>:

docker-compose run djangoapp sh -c "python djangoapp/manage.py test <app> && flake8"

However, you might need to comment out the last line in settings.py (heroku settings)

Currently not working:
- Celery beat (background jobs not functional)
- Not fully deployed to Heroku yet



Offers microservice

Base URL: Hidden (Environment variable)

Auction microservice

Base URL (Browseable API): http://www.product-api.me


ENDPOINTS:

POST /api/user/create/

Request:
{
  'email': <email>,
  'password': <password>,
  'name': <name>
}
Response:
201 CREATED
{
  'email': <email>,
  'name': <name>'
}
400 BAD REQUEST
{
  'email': <message>,
  'password': <message>,
  'name': <message>
}

POST /api/auction/product/

Authorization: <credentials>
Request:
{
  'name': <name>,
  'description': <description>
}
Response:
201 CREATED
{
  'id': <id>,
  'name': <name>,
  'description': <description>,
  'offers': []
}
400 BAD REQUEST
{
  'name': [<message>]
}
403 FORBIDDEN
{
  'detail': 'Invalid username/password.'
}

GET /api/auction/product/

Authorization: <credentials>
Request: None
Response:
200 OK
[
  {
    'id': <id>,
    'name': <name>,
    'description': <description>,
    'offers': [
      '<offer.name>: $<offer.price> (<offer.items_in_stock> in stock)',
      .
      .
      .
    ]
  },
  .
  .
  .
]
403 FORBIDDEN
{
  'detail': 'Invalid username/password.'
}

GET /api/auction/product/<id>/

Authorization: <credentials>
Request: None
Response:
200 OK
{
  'id': <product.id>,
  'name': <product.name>,
  'description': <product.description>,
  'offers': [
    {
      'id': <offer.id>,
      'price': <offer.price>,
      'items_in_stock': <offer.items_in_stock>
    },
    .
    .
    .
  ]
}
403 FORBIDDEN
{
  'detail': 'Invalid username/password.'
}
404 NOT FOUND
{
  'detail': 'Not found.'
}

PUT/PATCH /api/auction/product/<id>/
Authorization: <credentials>
Request:
{
  'name': <new_name>,
  'description': <new_description>
}
Response:
200 OK
{
  'id': <product.id>,
  'name': <product.new_name>,
  'description': <product.new_description>,
  'offers': [
    {
      'id': <offer.id>,
      'price': <offer.price>,
      'items_in_stock': <offer.items_in_stock>
    },
    .
    .
    .
  ]
}
400 BAD REQUEST
{
  'name': [<message>]
}
403 FORBIDDEN
{
  'detail': 'Invalid username/password.'
}
404 NOT FOUND
{
  'detail': 'Not found.'
}

DELETE /api/auction/product/<id>/
204 NO CONTENT

403 FORBIDDEN
{
  'detail': 'Invalid username/password.'
}
404 NOT FOUND
{
  'detail': 'Not found.'
}
