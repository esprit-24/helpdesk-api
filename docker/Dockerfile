FROM python:3.13-slim

WORKDIR /app

COPY requirements/development.txt ./requirements/development.txt

RUN pip install --no-cache-dir -r requirements/development.txt

COPY . .

CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8000"]
