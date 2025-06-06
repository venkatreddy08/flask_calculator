FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 5000


CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
