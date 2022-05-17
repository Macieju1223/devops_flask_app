FROM python:3.9-slim-buster

RUN mkdir /usr/src/app_test
COPY . /usr/src/app_test

WORKDIR /usr/src/app_test
EXPOSE 6666

RUN pip install -r requirements.txt
CMD ["pylint", "test_app.py"]