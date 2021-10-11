# FSND_CapStone

# Full Stack API Final Project
This project was built to test my knowledge of writing API endpoints and authentication 

All backend code follows PEP8 style guidelines.
## Getting started
### Pre-requisites and Local Development
Developers using this project should have python3 and pip installed on their local machines

#### Backend
From the backend folder run ```pip install -r requirements.txt``` All required packages are included in the requirements file.

To set up the database: 

```createdb Casting -U postgres``` 

To run the application run the following commands:
```
Set FLASK_APP=app.py
Set FLASK_ENV=development
python -m flask run
```
These commands put the application in development. Working in development mode shows an interactive debugger in the console and restarts the server whenever changes are made. if running locally on linux look for commands in the [Flask documentation](http://flask.pocoo.org/docs/1.0/tutorial/factory/).
The application on `http://127.0.0.1:5000` by default and on `https://casting101.herokuapp.com/`

### Tests
In order to run tests navigate to the backend folder and run the following commands:

```
dropdb casting_test -U postgres 

createdb casting_test -U postgres 

psql -U postgres casting_test < casting.pgsql

python test_app.py
```
The first time you run the tests, omit the dropdb command.
All tests are kept in that file and should be maintained as updates are made to app functionality.

## API Documentation

### Getting started

- Base url: At present this app can be at "https://casting101.herokuapp.com/"

- Authentication: you need to signup/login from this page```https://dev-g-z09scw.us.auth0.com/authorize?audience=Casting&response_type=token&client_id=Rz6YyS9V9I8ghwu3fY0ark7zACP5CHNQ&redirect_uri=https://casting101.herokuapp.com/actors```

### Error Handling
Erros are returnd as JSON objects in the following format:
```
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```
#### Response codes
 - 404: resource not found
 - 422: unprocessable
 - 400: bad request
 - 405: method not allowed

### Endpoints
The endpoints samples can be run throught postman

#### GET /actors
- General:
	- Returns a list of actors and success value
- Sample: https://casting101.herokuapp.com/actors
```
{                         
  "actors": [
        {
            "age": "24",
            "gender": "male",
            "id": 1,
            "name": "ahmed"
        },
        {
            "age": "23",
            "gender": "male",
            "id": 2,
            "name": "mohammed"
        }
    ],                 
  "sucess": true          
}                         
```


#### GET /movies
- General:
	- Returns a list of movies, success value, and total number of movies
	- Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.
- Sample: curl https://casting101.herokuapp.com/movies
```

   {
    "movies": [
        {
            "date": "01/15/2012",
            "id": 1,
            "title": "interstaller"
        }
    ],
    "success": true,
    "total_movies": 1
}
```
#### POST /actors

- General:
	- Creates a new actor using the name, age, and gender. Returns the created actor, success value and total actors.
- Sample: POST: https://casting101.herokuapp.com/actors
```
{
    "actors": [
        {
            "age": "23",
            "gender": "male",
            "id": 1,
            "name": "ahmed"
        },
        {
            "age": "23",
            "gender": "male",
            "id": 2,
            "name": "mohammed"
        }
    ],
    "created": {
        "age": "23",
        "gender": "male",
        "id": 4,
        "name": "khalid"
    },
    "success": true
}
```
#### POST /movies

- General:
	- Creates a new movie using the title and date. Returns the created movie, success value and total movies.
- Sample: POST: https://casting101.herokuapp.com/movies
```
{
    "created": {
        "date": "01/15/2012",
        "id": 1,
        "title": "interstaller"
    },
    "movies": [
        {
            "date": "01/15/2012",
            "id": 1,
            "title": "interstaller"
        }
    ],
    "success": true
}
```
#### DELETE /actors

- General:
	- Deletes the actor of the given ID if it exists. returns the success value, and the deleted actor.

- Sample: DELETE: https://casting101.herokuapp.com/actors
```
{
    "delete": {
        "age": "23",
        "gender": "male",
        "id": 10,
        "name": "mohammed"
    },
    "success": true
}
```

#### DELETE /movies

- General:
	- Deletes the movie of the given ID if it exists. returns the success value, and the deleted movie.

- Sample: DELETE: https://casting101.herokuapp.com/movies
```
{
    "delete": {
        "date": "01/15/2012",
        "id": 1,
        "title": "interstaller"
    },
    "success": true
}
```

#### PATCH /actors

- General:
	- Edit the actor of the given ID if it exists. returns the success value, and the edited actor.

- Sample: PATCH: https://casting101.herokuapp.com/actors
```
{
    "actors": {
        "age": "25",
        "gender": "male",
        "id": 2,
        "name": "khalid"
    },
    "success": true
}
```

#### PATCH /movies

- General:
	- Edit the movie of the given ID if it exists. returns the success value, and the edited movie.

- Sample: PATCH: https://casting101.herokuapp.com/movies
```
{
    "movies": {
        "date": "03/25/2006",
        "id": 3,
        "title": "catch me if you can"
    },
    "success": true
}
```

## Roles & Permsissions

### Casting Assistant
Can view actors and movies.
GET /movies, GET /actors
### Casting Director
All permissions a Casting Assistant has and…
Add or delete an actor from the database
Modify actors or movies.
GET /movies, GET /actors, POST /actors, PATCH /actors, PATCH /movies, DELETE /actors
### Executive Producer
All permissions a Casting Director has and…
Add or delete a movie from the database
GET /movies, GET /actors, POST /actors, PATCH /actors, PATCH /movies, DELETE /actors, POST /movies, DELETE /movies

  

                                                                                

## Deployment 
https://casting101.herokuapp.com

## Authors
Yours truly, Mohammed Alessa

## Acknowledgements
The awesome team at udacity


setup.sh has tokens that can be used to test different users using postman bearer token


