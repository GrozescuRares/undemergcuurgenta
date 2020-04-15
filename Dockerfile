FROM python:3.7.5-buster
# set work directory
WORKDIR /opt/undegasescacum

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

# copy project
COPY . /opt/undegasescacum/
