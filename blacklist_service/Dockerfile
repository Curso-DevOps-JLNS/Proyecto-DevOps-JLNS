FROM python:3.8-slim

WORKDIR /app

# Instala dependencias necesarias (incluye netcat)
RUN apt-get update && apt-get install -y netcat-openbsd && apt-get clean

#COPY newrelic_local.ini /app/newrelic.ini
COPY newrelic.ini /app/newrelic.ini
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

#CMD ["python", "run.py"]
CMD ["newrelic-admin", "run-program", "python", "run.py"]