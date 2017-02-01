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

gunicorn -w 4 mysite.wsgi:apllication &  
sudo nano /etc/nginx/sites-available/myprojectserver  

###server configration

server {  
   </t> listen 80;  
   </t> server_name 38.76.11.161  
   </t> access_log off;  
    
   </t> location /static/ {  
   </t></t>     alias /home/ubuntu/work/myproject/static/;  
  </t></t>    }  

   </t>  location / {  
    </t></t>  proxy_pass http://127.0.0.1:8000;  
 </t></t>     }    
}  

cd /etc/nginx/sites-enabled  
sudo ln -s ../sites-available/myproject  
sudo rm default  
sudo service nginx restart  
