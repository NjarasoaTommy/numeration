FROM python:3.12-slim

WORKDIR /my_project

COPY /outils ./outils
COPY /unit_tests ./unit_tests
COPY main.py .

RUN pip install pytest