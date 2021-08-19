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

NOTES for Admin:
After creating admin user by command createsuperuser
You need get Token on /login/ endpoint which you need to send to the body username and password.

and your API requests should have an Authentication header.

