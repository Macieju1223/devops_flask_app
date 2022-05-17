FROM python:3.9-slim-buster
RUN mkdir /usr/src/app/
COPY . /usr/src/app/
WORKDIR /usr/src/app/
EXPOSE 5555
RUN pip install -r requirements.txt
CMD ["python", "app.py"]