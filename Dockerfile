FROM python:3.8-slim-buster
WORKDIR /code
ENV FLASK_APP=api.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5666
# RUN apt install gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 5666
COPY . .
CMD ["flask", "run"]