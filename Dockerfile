FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD python -m uvicorn main:app --reload

EXPOSE 8000