FROM python:3.12-slim

WORKDIR /app

COPY api.py .
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["python", "api.py"]

