FROM python:3.10-alpine
RUN pip install -U celery[redis]
COPY main.py tasks.py /app/
WORKDIR /app
