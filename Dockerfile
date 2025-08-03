FROM python:3.10-slim
LABEL authors="Ayan"

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache -r requirements.txt

EXPOSE 80

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

