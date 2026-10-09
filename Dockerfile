FROM python:3.12-slim

WORKDIR /app

COPY app.py .
COPY sample_invoice.txt .

CMD ["python", "app.py"]
