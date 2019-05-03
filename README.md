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

## Sign-Up Process:

For User Registration:
    http://localhost:8000/api/user/signup/
    
    parameters:
        username,first name, last name,password
## Login Process:

For Login:
    http://localhost:8000/api-auth/login
    
    parameters: 
        username,password
        
For Logout:
    http://localhost:8000/api-auth/logout

## Posts:

For Posts:
    http://localhost:8000/api/posts/
    
    parameters:
        Title,Content

For Follow:
    http://localhost:8000/followers/
    
    parameters:
        select the user to follow

For Like:
    http://localhost:8000/api/like
    
    parameters:
        select the post to like
        
 For Comment:
    http://localhost:8000/api/comment
    
    parameters:
        select the post to comment
