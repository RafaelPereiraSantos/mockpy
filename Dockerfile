FROM python:3-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN python3 -m pip install --upgrade -r requirements.txt
COPY . .
RUN cp .env-template .env

EXPOSE 3001:3001


CMD [ "python3", "./main.py" ]