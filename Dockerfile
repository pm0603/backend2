FROM        eb-base
MAINTAINER  archoiym@gmail.com


WORKDIR     /srv
RUN         mkdir app
WORKDIR     /srv/app
RUN         mkdir backend
WORKDIR     /srv/app/backend

COPY        . /srv/app/backend

#RUN         pip3 install -r requirements.txt

COPY        .conf/uwsgi-app.ini         /etc/uwsgi/sites/mysite.ini
COPY        .conf/nginx.conf            /etc/nginx/nginx.conf
COPY        .conf/nginx-mysite.conf     /etc/nginx/sites-available/mysite.conf
COPY        .conf/supervisor-app.conf   /etc/supervisor/conf.d/
RUN         ln -s /etc/nginx/sites-available/mysite.conf /etc/nginx/sites-enabled/mysite.conf

EXPOSE      80
CMD         supervisord -n