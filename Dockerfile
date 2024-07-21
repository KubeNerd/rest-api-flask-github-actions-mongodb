FROM python:3.9.12-alpine3.15

WORKDIR /app

COPY requirements.txt wsgi.py config.py ./

COPY application ./application

RUN pip install -r requirements.txt


EXPOSE 5000

CMD ["python3", "wsgi.py"]
