FROM        ubuntu:16.04
MAINTAINER  archoiym@gmail.com

RUN         apt-get -y update
RUN         apt-get -y install python3
RUN         apt-get -y install python3-pip
RUN         apt-get -y install nginx
RUN         apt-get -y install supervisor

RUN         pip3 install uwsgi

WORKDIR     /srv
RUN         mkdir app
WORKDIR     /srv/app

COPY        . /srv/app
RUN         pip3 install -r requirements.txt

COPY        .conf/uwsgi-app.ini         /etc/uwsgi/sites/mysite.ini
COPY        .conf/nginx.conf            /etc/nginx/nginx.conf
COPY        .conf/nginx-mysite.conf     /etc/nginx/sites-available/mysite.conf
COPY        .conf/supervisor-app.conf   /etc/supervisor/conf.d/
RUN         ln -s /etc/nginx/sites-available/mysite.conf /etc/nginx/sites-enabled/mysite.conf

EXPOSE      4040
CMD         supervisord -n