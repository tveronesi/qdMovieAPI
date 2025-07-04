FROM python:3.12-slim

WORKDIR /app

COPY main.py .
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["python", "main.py"]

# run on the root directory :
#    docker build -t qd_imdb_api .

# docker run -it --rm -p 5000:5000 -v $PWD:/app -w /app  qd_imdb_api python main.py
