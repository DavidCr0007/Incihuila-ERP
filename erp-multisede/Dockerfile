FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements ./requirements
RUN pip install --upgrade pip \
    && pip install -r requirements/prod.txt

COPY src ./src
COPY deploy ./deploy

ENV DJANGO_SETTINGS_MODULE=erp.settings.production

EXPOSE 8000

CMD ["gunicorn", "-c", "deploy/gunicorn.conf.py", "erp.wsgi:application"]
