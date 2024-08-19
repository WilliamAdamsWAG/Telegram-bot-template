FROM python:3-slim

ENV TELEGRAM_API_TOKEN="your_token"

ADD . ./app

WORKDIR /app/src
RUN pip install -r requirements.txt
CMD python main.py