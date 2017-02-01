# twitter-clone
Inital Steps to run the project

Make sure you run this in new vitual environment

In case you have no idea about how to create virtual env then follow this http://docs.python-guide.org/en/latest/dev/virtualenvs/

$ cd twitter-clone
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
And it's done! Enjoy..


#Running the same project on nginx

pip install -r requirements.txt
  ./manage.py makemigrations  
  ./manage.py migrate  
  ./manage.py loaddata sites  
  ./manage.py collectstatic  
  
##Starting Gunicorn
