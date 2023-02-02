FROM python:3.7.0

RUN apt-get update \
&& apt-get install -y postgresql postgresql-contrib libpq-dev python3-dev \
&& apt install sshpass

COPY requirements.txt .
RUN pip3 install --upgrade pip -r requirements.txt

COPY ./ ./

RUN chmod +x wait-for-postgres.sh
