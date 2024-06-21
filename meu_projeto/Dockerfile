# Dockerfile

FROM python:3.12

WORKDIR /app

COPY requirements.txt requirements.txt
COPY app.py app.py
COPY model.pkl model.pkl

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
