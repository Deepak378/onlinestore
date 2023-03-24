FROM python:3.9-slim-buster

WORKDIR /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY . .

CMD ["python", "online_store_analysis.py"]

CMD ["python", "-m", "unittest", "test_revenue_analysis.py"]
