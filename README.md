# Back-end-Lab-1

## Introduction
This document contains instructions for running the project locally and using Docker, Docker Compose.

## Requirements
- Python 3.11(or higher)
- Docker
- Docker Compose

## Starting a local project

### Your actions:
1. Clone repository
```bash
git clone <repository url>
cd <repository location>
```
2. Create and activate virtual environment
```bash
python -m venv env
.\env\Scripts\activate
```
3. Download requirements
```bash
pip install -r requirements.txt
```
4. Start server
```bash
flask --app app run --host 0.0.0.0 --port 5000 
```
5. Checking on workability
```bash
http://localhost:5000/healthcheck
```

## Starting project with Docker

### Your actions:
1. You need to create and fill Dockerfile
```bash
FROM python:3.12.3-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY . /app

CMD flask --app app run -h 0.0.0.0 -p $PORT

```
2. Then build dockefile
```bash
docker build . -t <image_name>:latest
``` 
3. Try to run and test image
```bash
docker run -it --rm -e PORT=<port_number> -p <port_number>:<port_number> <image_name>:latest
```
## Starting project with Docker Compose

### Your actions:
1. You need to create and fill docker-compose.yaml
```bash
version: '3'

services:
  web:
    restart: always
    build:
      context: .
      dockerfile: Dockerfile
    environment:
      PORT: "8080"
    ports:
      - "8080:8080"
```

2. Then build it
```bash
docker-compose build
```
3. And try to run and test
```bash
docker-compose up
```

## Deploying
You also can try to deploy this app

I use [Render.com](https://dashboard.render.com/) for duing this

[URL for my project](https://back-end-lab-1-ulih.onrender.com/healthcheck)
