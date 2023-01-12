FROM python:3.8
# set work directory
WORKDIR /usr/src/app/producer
# copy project
COPY . /usr/src/app/producer
# install dependencies
RUN pip install --user pika
# run app
CMD ["python", "producer.py"]