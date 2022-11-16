FROM python:3.10
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
CMD ["alembic", "upgrade", "head"]
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]