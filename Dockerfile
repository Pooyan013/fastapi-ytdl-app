FROM python:3.9-slim

WORKDIR /app

COPY . /app
COPY templates /app/templates
COPY static /app/static

RUN pip install --no-cache-dir -r requierment.txt 

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0","--port","8000"]