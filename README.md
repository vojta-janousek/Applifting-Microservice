# Applifting-Microservice

IMPORTANT:

- Endpoint documentation is in the ENDPOINTS.md file
- Environment variables are hidden and ignored by git
- Application uses PostgreSQL
- You can use the following command to run unit tests on core app (or replace with auction):

docker-compose run djangoapp sh -c "python djangoapp/manage.py test core && flake8"

However, you need to comment out the last line in settings.py (heroku settings)


Thursday: Project setup

- Created and initialised a GitHub repository
- Created and configured a Dockerfile
- Created a requirements.txt file
- Created a docker-compose.yml configuration
- Built a Docker image

- Created a .travis.yml file
- Activated Travis on the GitHub repository
- Created a .flake8 file for linting exclusions
- Created a Procfile for future Heroku deployment

- Created a Django project
- Configured the .gitignore file
- Created a settings.ini file with environment variables

- Created app called 'auction'
- Changed database from sqlite to postgresql
- Configured project settings
- Made migrations to the new database

Friday:

- Created app called 'core'
- Added a test for wait_for_db functionality (core)
- Implemented wait_for_db functionality (core)

(core):
- Added a test for a custom user model being created
- Created a custom user model and a custom user manager
- Added a test for email normalization
- Implemented email normalization feature
- Added a test for email field validation
- Implemented email field validation feature
- Added a test for a custom superuser being created
- Implemented a method for creating superusers
- Added tests for listing, creating and changing users in the admin interface
- Implemented the above features

Saturday:

(auction):
- Added tests for the models' string representation
- Created Product and Offer models
- Migrated both models and registered them to the admin interface

- Added tests for retrieving products by authorized and unauthorized users
- Created a product serializer
- Created a product list view and registered it to the url router

- Added a test for checking that products are limited to their users
- Configured querysets to filter products by their user

- Added tests for creating a new product with valid and invalid payloads
- Configured product view to include create model feature
