FROM python:3.7.3

WORKDIR /usr/src/app

COPY api_service.py .
COPY utils.py .
COPY requirements.txt .
COPY wait-for-it.sh .

RUN pip install --no-cache-dir -r requirements.txt

