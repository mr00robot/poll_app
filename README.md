# Poll API

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/timur737/poll_app.git
$ cd poll_app
```
And you need create virtualenv
```sh
$ python3.9 -m venv venv
$ . venv/bin/activate
```
After that
```sh
$ pip install -r requirements.txt
$ python manage.py makemigrations && python manage.py migrate
$ python manage.py runserver
```
List of endpoints you can see in http://127.0.0.1:8000/swagger/

BASE endpoint : ```http://127.0.0.1:8000/api/v1/```

NOTES for Admin:
After creating admin user by command createsuperuser
You need get Token on /login/ endpoint which you need to send to the body username and password.

and your POST, PUT, PATCH, DELETE API requests should have an Authentication header.

For user:
You can get all your answer by ```GET /answer_user/{your_id}/```

- See all polls ```GET /polls/```
- Questions for polls ``` GET /questions/```
- If type of answer for question one choice or multiple choice, You can get choices in ```GET /choices/```
