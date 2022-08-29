FROM python:3.9
WORKDIR /usr/src/job_website
COPY . ./app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt