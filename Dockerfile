FROM python:3.10-slim
LABEL authors="Ayan"

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache -r requirements.txt

COPY . ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
