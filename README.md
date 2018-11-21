# Deployer

## Note
This should be deployed on the same server running *Dokku*, if you need some guide on How To Deploy Django on Nginx, [check here](http://www.timtech4u.com.ng/2018/06/how-to-set-up-django-with-postgres.html)

## Setup
- Clone the repo and change to project directory: `cd pusher`
- Install dependencies: `pip install -r requirements.txt`
- Migrate database: `python manage.py migrate`
- Create super user: `python manage.py createsuperuser`
- Run server: `python manage.py runserver`
