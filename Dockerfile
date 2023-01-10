FROM python:3.8
# set work directory
WORKDIR /usr/src/app/
# copy project
COPY telegram_bot /usr/src/app/
COPY test_audio /usr/src/test_audio/
# install dependencies
RUN pip install --user aiogram
# run app
CMD ["python", "bot.py"]