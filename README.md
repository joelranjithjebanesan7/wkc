# Setting up the project

create virtualenv:

`virtualenv -p python3 env`

Activate the environment: 

`source env/bin/activate`

Into the project  directory:

`pip install -r requirements.txt`

## Setting database:
In tasks/settings.py: configure the database and database user credentials.

Migrate the changes:
  `python manage.py makemigrations`
  
  `python manage.py migrate`

Run the server: 
 `python manage.py runserver`

## URLs:
For User Registration:
    http://localhost:8000/user/signup/

For Login:
    http://localhost:8000/api-auth/login
    
For Logout:
    http://localhost:8000/api-auth/logout

For Posts:
    http://localhost:8000/api/posts/

For Follow:
    http://localhost:8000/followers/

For Like:
    http://localhost:8000/api/like
 
 For Comment:
    http://localhost:8000/api/comment
