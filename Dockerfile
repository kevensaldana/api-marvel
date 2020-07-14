FROM python:3.7

RUN pip install \
  fastapi \
  uvicorn \
  httpx \
  dependency-injector \
  python-dotenv

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--workers","3"]

EXPOSE 80