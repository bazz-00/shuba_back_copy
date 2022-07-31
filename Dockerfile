FROM python:3.9.7
# set work directory
WORKDIR /usr/src/Shuba_back
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .

RUN pip install -r requirements.txt
# copy project
COPY . .