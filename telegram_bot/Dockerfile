FROM python:3.8
# set work directory
# copy project

# install dependencies
RUN pip install --user aiogram
RUN pip install pika
RUN pip install google-api-python-client
COPY . /src/bot
# run app
ENTRYPOINT ["python", "./src/bot/bot.py"]