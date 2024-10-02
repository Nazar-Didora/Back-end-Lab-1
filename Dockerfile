FROM python:3.12.3-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY . /app

CMD flask --app app run -h 0.0.0.0 -p $PORT
