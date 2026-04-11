FROM python:3.12-slim

WORKDIR /my_project

COPY /outils ./outils
COPY /unit_tests ./unit_tests
COPY main.py .
COPY conftest.py .

RUN pip install pytest

CMD ["/bin/bash"]