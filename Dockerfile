FROM python:3.9.8-alpine3.14

WORKDIR app

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]