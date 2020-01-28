1) Project setup

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

2) Database configuration

- Created app called 'core'
- Added a test for wait_for_db functionality (core)
- Implemented wait_for_db functionality (core)

3) Custom user model (core)

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

4) Model creation (auction)

- Added tests for the models' string representation
- Created Product and Offer models
- Migrated both models and registered them to the admin interface

5) Product creating and retrieving (auction)

- Added tests for retrieving products by authorized and unauthorized users
- Created a product serializer
- Created a product list view and registered it to the url router

- Added a test for checking that products are limited to their users
- Configured querysets to filter products by their user

- Added tests for creating a new product with valid and invalid payloads
- Configured product view to include create model feature

- Created tests for displaying a product detail
- Configured serialized CRUD functionality for product model

- Configured CRUD endpoints via Router

6) User management endpoints (user)

- Created app called 'user'
- Added tests for successfully creating a new user
- Added a test creating an existing user to fail
- Added a test checking if the selected password is longer than 5 characters
- Created user model serializer and serialized view
- Assigned url to the view

- Added a test to make sure users always have to be authenticated
- Added a test to make sure a profile can be retrieved
- Added a test to make sure post request is not allowed on this urls
- Added tests to make sure users can update their profiles
- Created a view for authenticated user management and assigned a url to it

7) Sending requests to Products microservice (auction/requests)

- Added requests package to requirements.txt
- Added login/logout feature to the browseable API
- Tested requests for user creation/authentication
- Tested requests for product CRUD

8) Sending requests to Offers microservice (auction/requests)

- Requested an access token and saved it as an environment variable
- Registered a test product
- Tested retrieving all offers for the registered product
- Tested the number of mutual offers in consecutive get requests

9) Offer model changes (auction)

- Fixed Offer model to work with incoming data
- Added tests for the new Offer model

10) Microservice integration

- Created a signal that registers a new product that has been created
- Tested the signal

- Added Celery and Redis to requirements.txt
- Built images for both, linked them together, along with db
- Configured project for Celery, created test tasks

11) Background jobs

- Created a command for updating offers of a selected product
- Tested and linked the command to celery tasks file
- Added current average price and price percentage change fields to Product model
- Added a command to calculate both from old data and new request query
- Tested the new command

12) Miscellaneous

- Added endpoint documentation to the README.md file
- Converted Offer MS base URL to an environment variable
- Added a landing page
- Ran all tests

13) Deployment to Heroku

- Hid the database password
- Created a Heroku project
- Found, bought and registered a custom domain to the Heroku project
