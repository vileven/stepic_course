#nginx conf
sudo rm -r /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

#gunicorn conf
sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/ask_volodin
sudo /etc/init.d/gunicorn restart


