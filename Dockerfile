FROM python:2
WORKDIR /home/app
COPY ./ /home/

RUN pip install flask psycopg2 flask-sqlalchemy requests

CMD ["python", "server.py"]