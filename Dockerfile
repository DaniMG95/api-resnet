FROM python:3.7.12-alpine3.14

EXPOSE 5000

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD python3 server.py