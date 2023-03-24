FROM python:3.9-slim-buster

WORKDIR /app

COPY orders.csv .

RUN pip install --no-cache-dir -r orders.csv

COPY . .

CMD ["python", "online_store_analysis.py"]
