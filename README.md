# social_network_analisys
This project will allow to carry out an analysis of people mood based on their social network activity

## Little Guide to run project locally

1. Cloning Git-repository:
$ sudo apt-get install git
$ mkdir dir_name
$ cd dir_name
$ git init
$ git clone https://github.com/MarinaMeyta/social_network_analisys.git
$ cd social_network_analisys/

2. Activating virtual environment:
$ source djenv/bin/activate
To deactivate venv, just type:
$ deactivate

3. Installing [Django](https://www.djangoproject.com/):
$ sudo apt-get install python-pip
$ pip install django==1.8

4. Installing [tweepy](https://github.com/tweepy/tweepy):
$ pip install tweepy

5. Running local server
$ python manage.py runserver
