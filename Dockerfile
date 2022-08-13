FROM python:latest

WORKDIR /my_code

COPY . .

RUN pip install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:1234 my_app:app

