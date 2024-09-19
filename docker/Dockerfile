FROM python:3.9-slim

WORKDIR /usr/src/app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Run the application using gunicorn
CMD ["flask", "run", "--host=0.0.0.0"]