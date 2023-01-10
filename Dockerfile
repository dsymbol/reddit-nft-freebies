FROM python:3.11-alpine3.17

WORKDIR app

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]
