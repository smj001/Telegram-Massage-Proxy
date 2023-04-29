FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV API_KEY=YOUR_SECRET_API_KEY_HERE

EXPOSE 5000

CMD ["python", "app.py"]
