# Applifting-Microservice

IMPORTANT:

- Endpoint documentation is in the ENDPOINTS.md file
- Environment variables are hidden and ignored by git
- Application uses PostgreSQL


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
- Added tests for wait_for_db functionality (core)
- Implemented wait_for_db functionality (core)

(core):
- Added test for a custom user model being created
- Created a custom user model and a custom user manager
- Added test for email normalization
- Implemented email normalization feature
- Added test for email field validation
- Implemented email field validation feature
- Added test for a custom superuser being created
- Implemented a method for creating superusers


- Created Product and Offer models (auction)
