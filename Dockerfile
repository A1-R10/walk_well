FROM python:3.10-slim-bullseye
ENV ENPYTHONUNBUFFERED=1
WORKDIR /walk_well

COPY requirements.txt requirements.txt

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
