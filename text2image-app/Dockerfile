# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Préparer l'environnement
COPY requirements.txt /app/requirements.txt
RUN apt-get update && apt-get install -y git build-essential libsndfile1 ffmpeg && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copier l'app
COPY . /app

EXPOSE 7860

ENV GRADIO_SERVER_NAME=0.0.0.0
ENV GRADIO_SERVER_PORT=7860

CMD ["python", "app/main.py"]
