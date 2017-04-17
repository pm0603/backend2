# 처음부터 도커 이미지 생성 시
#FROM        ubuntu:16.04
#MAINTAINER  archoiym@gmail.com

# 필요한 파일 변경사항 및 패키지 설치(배포용)
FROM        archoiym/pm0603:latest
MAINTAINER  archoiym@gmail.com

# 중복되는 기본 설치 항목(base-1)
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

# pip패키지가 변한 경우
#WORKDIR     /srv/app
#RUN         pip3 install -r requirements.txt && \
#            pip3 install uwsgi


# 오류 나는 NPM 관련 부분(base-npm)
#FROM        base-1
#MAINTAINER  archoiym@gmail.com
#WORKDIR     /srv/app/front
#RUN         npm install
#RUN         npm run build

# 배포 시 서버 설정이 바뀐 경우
#COPY        .conf/uwsgi-app.ini /etc/uwsgi/sites/app.ini
#COPY        .conf/nginx-app.conf /etc/nginx/sites-available/app
#COPY        .conf/nginx.conf /etc/nginx/nginx.conf
#COPY        .conf/supervisor-app.conf /etc/supervisor/conf.d/
#RUN         ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled/app

# 기본 실행 부분 (배포용)
COPY        . /srv/app
WORKDIR     /srv
RUN         git clone https://github.com/pm0603/frontend-vue.git frontend
WORKDIR     /srv/app/django_app
EXPOSE      4567
CMD ["supervisord", "-n"]

#-----------------------------------------------

# NPM설치 처음부터 TEST

#FROM        ubuntu:16.04
#MAINTAINER  archoiym@gmail.com
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
#WORKDIR     /srv/app/front
#RUN         npm install
#RUN         npm run build
#
#COPY        .conf/uwsgi-app.ini /etc/uwsgi/sites/app.ini
#COPY        .conf/nginx-app.conf /etc/nginx/sites-available/app
#COPY        .conf/nginx.conf /etc/nginx/nginx.conf
#COPY        .conf/supervisor-app.conf /etc/supervisor/conf.d/
#RUN         ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled/app
#
#WORKDIR     /srv/app/django_app
#EXPOSE      4567
#CMD ["supervisord", "-n"]