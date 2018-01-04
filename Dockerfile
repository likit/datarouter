FROM python:2
WORKDIR /home/app

RUN pip install flask psycopg2 flask-sqlalchemy requests

CMD ["python"]