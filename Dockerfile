FROM python:3.12-slim

# install git
RUN apt-get update && \
    apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /app

COPY api.py .
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["python", "api.py"]

# run on the root directory :
#    docker build -t qd_imdb_api .

# docker run -it --rm -p 5000:5000 -v $PWD:/app -w /app  qd_imdb_api python api.py
