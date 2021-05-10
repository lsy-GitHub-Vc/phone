FROM python:3.6
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt 
RUN mkdir -p /var/log/uwsgi
RUN touch /var/log/uwsgi/uwsgi.log
RUN apt-get update && \
    apt-get install -y vim 
ADD . /code
# RUN pip install future
# RUN apt-get update
# RUN apt-get install vim

