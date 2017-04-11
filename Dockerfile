#FROM        pray
FROM        archoiym/front:latest
#FROM        production-without-node-execution-and-npm-run-build
MAINTAINER  archoiym@gmail.com

#COPY        . /srv/app
#RUN         apt-get -y update && \
#            apt-get -y install python3 && \
#            apt-get -y install python3-pip && \
#            apt-get -y install nginx && \
#            apt-get -y install supervisor
#
#RUN         apt-get -y install git && \
#            apt-get -y install curl && \
#            apt-get -y install libcurl4-openssl-dev && \
#            apt-get -y install libssl-dev && \
#            curl -sL https://deb.nodesource.com/setup_6.x | bash - && \
#            apt-get -y install nodejs
#
#WORKDIR     /srv/app
#RUN         pip3 install -r requirements.txt && \
#            pip3 install uwsgi
#
#WORKDIR     /srv
#RUN         git clone https://github.com/pm0603/frontend-vue.git front


#pray
#---------


#WORKDIR     /srv/front
#RUN         npm install
##RUN         npm run build
#
#COPY        .conf/uwsgi-app.ini /etc/uwsgi/sites/app.ini
#COPY        .conf/nginx-app.conf /etc/nginx/sites-available/app
#COPY        .conf/nginx.conf /etc/nginx/nginx.conf
#COPY        .conf/supervisor-app.conf /etc/supervisor/conf.d/
#RUN         ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled/app

WORKDIR     /srv/app/django_app
EXPOSE      4567
CMD ["supervisord", "-n"]