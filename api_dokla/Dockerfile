
FROM python:3.9

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/
COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Définir la commande de démarrage
CMD ["python", "manage.py", "runserver"]
