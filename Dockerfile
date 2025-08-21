FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip  \
    && pip install -r requirements.txt

COPY api.py .

EXPOSE 5000
ENTRYPOINT ["python", "api.py"]

# build command
# docker build -t qd_imdb_api .