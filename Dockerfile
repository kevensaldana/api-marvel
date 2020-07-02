FROM python:3.7

RUN pip install fastapi uvicorn httpx dependency-injector

COPY ./pyproject.toml ./poetry.lock* /app/

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

EXPOSE 80