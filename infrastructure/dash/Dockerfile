# dash_app/Dockerfile

FROM python:3.12-slim

WORKDIR /app

COPY infrastructure/dash/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app

CMD ["python", "-m", "dash_app.app"]
