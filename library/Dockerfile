from python:3.8.6

RUN apt-get update && apt-get install -y postgresql-contrib
RUN pip3 install --upgrade pip
COPY ./ ./
RUN pip3 install -r requirements.txt

RUN pip3 install gunicorn

RUN chmod +x wait-for-postgres.sh