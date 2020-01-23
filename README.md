# nomaCakes

[![Coverage Status](https://coveralls.io/repos/github/kizzanaome/nomaCakes/badge.svg?branch=develop)](https://coveralls.io/github/kizzanaome/nomaCakes?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/c083d388535220ba5ccd/maintainability)](https://codeclimate.com/github/kizzanaome/nomaCakes/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/c083d388535220ba5ccd/test_coverage)](https://codeclimate.com/github/kizzanaome/nomaCakes/test_coverage)

This is a small web app for a cake business, nomaCakes.co that allows customers to lookup their best and desired cakes made by the company and purchase them, rate them, save them to a cart and review them.

## Pre-requists
The backend of the project is developed in Python Django with REST and the frontend is developed in AngularJS, the database being used here is PostgreSQL

## Getting started
Open up your terminal and navigate to your preferred storage point and then clone the repository to your computer by typing this command
```
    git clone https://github.com/kizzanaome/nomaCakes.git
``` 
Navigate into the nomaCakes folder created after the clone and in it create a virtual environment with your preferred name by typing
```
    cd nomaCakes
    virtualenv yourpreferredname
```
If you prefer python 3 in the virtual environment, then type this instead
```
    virtualenv -p python3 noma-env
```
Activate your virtual environment
```
    <!-- for ubuntu or mac use this command -->
    source yourpreferredname/bin/activate
    <!-- for windows use this command -->
    yourpreferredname\Scripts\activate
```
Install the dependencies for the application found in the requirements file
```
  pip install -r requirements.txt
```
Install PostgreSQL and load the psql shell and in it create a database with your preferred name by typing this command
```
    psql CREATE DATABASE yourpreferredname
```
Create a .env file and populate it with your database credentials following the sample_env.txt file in the project

Run the migrations by typing this command
```
  python manage.py migrate
```
This will help you in populating your database

Run the application
```
    python manage.py runserver
```

You can use Postman to checkout the functionality of the api endpoints, you can download here:
- [Postman](https://www.getpostman.com/apps) - An API testing tool for developers
