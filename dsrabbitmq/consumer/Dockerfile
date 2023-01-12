FROM python:3.8
# set work directory
WORKDIR /usr/src/app/consumer
# copy project
COPY . /usr/src/app/consumer
# install dependencies
RUN pip install --user pika
# run app
CMD ["python", "consumer.py"]