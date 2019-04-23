# Setting up the project

create virtualenv:
virtualenv -p python3 env
Activate the environment: source env/bin/activate

`pip install -r requirements.txt`

## Setting database:
In tasks/settings.py: configure the database and database user credentials.
Run the server: python manage.py runserver

## URLs:
For User Registration:
    https://localhost:8000/user/signup/

For Login:
    https://localhost:8000/api-auth/login
    
For Logout:
    https://localhost:8000/api-auth/logout

For Posts:
    https://localhost:8000/api/posts/

For Follow:
    https://localhost:8000/followers/

For Like:
    https://localhost:8000/api/like
 
 For Comment:
    https://localhost:8000/api/comment
