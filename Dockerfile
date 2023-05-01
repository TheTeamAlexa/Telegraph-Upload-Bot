FROM python:3.9-slim-buster
WORKDIR /app
COPY . /app
RUN pip3 install --no-cache-dir --upgrade pip --requirement requirements.txt
CMD ["python3", "Alexa.py"]
