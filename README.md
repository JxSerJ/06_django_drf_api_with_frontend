# coursework_6

For build and launch use this command in project root directory:

`docker compose up --build -d`

This command will do the following:
 - create PostgreSQL database
 - perform all necessary migrations and load initial fixture data from **./skymarket/fixtures/**
 - build and launch django-based backend on gunicorn WSGI server
 - build frontend using source code from directory **./frontend_react/**
 - create nginx server to proxy data of all these containers

For db and backend build environment vars from .env file will be used.

Frontend will be on http://127.0.0.1:3000/

Backend will be on http://127.0.0.1:8000/

Use these credentials for login:

    For user

    Login: test@skypro.ru
    Password: 111
_


    For admin

    Login: admin@skypro.ru
    Password: 111


