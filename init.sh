chmod -R a+rw ../../
sudo pip3 install django
sudo pip3 install django-autofixture
sudo pip install django-autofixture
sudo pip3 install pymysql
sudo pip install pymysql

#nginx conf
sudo rm -r /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

#gunicorn conf
sudo rm -r /etc/gunicorn.d/test
sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart

#mysql
#sudo /etc/init.d/mysql start
#mysql -uroot -e "create database qa"




