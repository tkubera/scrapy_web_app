# pull official base image
FROM python:3.9
#FROM mcr.microsoft.com/playwright:v1.6.2-focal

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install --upgrade -r requirements.txt

RUN playwright install-deps

RUN playwright install

# copy project
COPY . /usr/src/app/
# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
