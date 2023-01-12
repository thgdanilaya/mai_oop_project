import config
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os
import pika
import aio_pika
import asyncio

import bot_consumer
import bot_producer

bot = Bot(token=config.TOKEN)
dispatch = Dispatcher(bot)

amqp_url = os.environ["AMQP_URL"]
url_params = pika.URLParameters(amqp_url)


@dispatch.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply("I am a bot that can generate music by your tastes. Use /menu to see functions")
    # print(message.from_user.id)


@dispatch.message_handler(commands=['menu'])
async def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("How are you")
    item2 = types.KeyboardButton("Generate for me")
    markup.add(item1, item2)
    # print(str(message.from_user.id) + "menu")
    await bot.send_message(message.chat.id, "Let's see ^w^", reply_markup=markup)


@dispatch.message_handler(commands=['generate'])
async def generator_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    await bot_producer.publish(message.chat.id)

    await bot.send_message(message.chat.id, "generating beat, it can take some time, pls WAIT",
                           reply_markup=markup)
    audio = open('../test_audio/hip-hop.mp3', 'rb')
    await bot.send_audio(message.chat.id, audio)


@dispatch.message_handler(commands=['ficha'])
async def ear_blood(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    await bot.send_message(message.chat.id, "sending trap, it can take some time, pls WAIT",
                           reply_markup=markup)
    audio = open('../test_audio/kentplant.mp3', 'rb')
    await bot.send_audio(message.chat.id, audio)


@dispatch.message_handler(content_types=['text'])
async def answer(message):
    if message.text == "Hello":
        await bot.send_message(message.chat.id, "Hello. What do you want from me?")
    elif message.text == "Generate for me":
        await send_beat(message)
    elif message.text == "How are you":
        await bot.send_message(message.chat.id, "I have problems with deadlines >.<")
    else:
        await bot.send_message(message.chat.id, "Idk what u said")


async def send_beat(message):
    markup_beat = types.ReplyKeyboardMarkup(resize_keyboard=True)
    await bot.send_message(message.chat.id,
                           "You can use /generate to start beat creating\nUse /ficha чтобы получить гарантированную кровь из ушей",
                           reply_markup=markup_beat)
    # print(str(message.from_user.id) + "generate")


if __name__ == "__main__":
    executor.start_polling(dispatch)
