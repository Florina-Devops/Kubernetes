FROM python:3.10-alpine
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python3", "/app/Flask website/flask-website.py"]