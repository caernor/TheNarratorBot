import telebot
from telebot import types 
import module as m 

bot = telebot.TeleBot('1318065893:AAHnEzfW1aMqHl5JPDu6G1qXWG8EFAhPIJs')

main = telebot.types.ReplyKeyboardMarkup(True, True)
main.row("расскажи стих", "информация о боте")

l2 = telebot.types.ReplyKeyboardMarkup(True, True)
l2.row("расскажи стих пушкина", "расскажи стих блока", "расскажи стих маяковский")

l2_2 = telebot.types.ReplyKeyboardMarkup(True, True)
l2_2.row("список авторов", "список стихов", "основная информация о боте", "меню")

l2_3 = telebot.types.ReplyKeyboardMarkup(True, True)
l2_3.row("стихи Пушкина", "стихи Блока", "стихи Маяковского")

l2_2_1 = telebot.types.ReplyKeyboardMarkup(True, True)
l2_2_1.row("список стихов пушкина")

l3_1 = telebot.types.ReplyKeyboardMarkup(True, True)
l3_1.row("следующий стих пушкина", "меню")

l3_2 = telebot.types.ReplyKeyboardMarkup(True, True)
l3_2.row("следующий стих блока", "меню")

l3_3 = telebot.types.ReplyKeyboardMarkup(True, True)
l3_3.row("следующий стих маяковского", "меню")

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id, 'привет, я бот который может расказывать стихи', reply_markup=main)

@bot.message_handler(content_types=['text'])
def send_text(message):
	#main
	if message.text.lower() == 'расскажи стих':
		bot.send_message(message.chat.id, 'стих какого автора вы хотите?', reply_markup=l2)
	elif message.text.lower() == 'информация о боте':
		bot.send_message(message.chat.id, 'что вы хотите узнать?', reply_markup=l2_2)
    #l2
	elif message.text.lower() == 'расскажи стих пушкина':
		bot.send_message(message.chat.id, m.p_random(), reply_markup=l3_1)
	elif message.text.lower() == 'расскажи стих блока':
		bot.send_message(message.chat.id, m.b_random(), reply_markup=l3_2)
	elif message.text.lower() == 'расскажи стих маяковский':
		bot.send_message(message.chat.id, m.m_random(), reply_markup=l3_3)
	#l2_2
	elif message.text.lower() == 'список авторов':
		bot.send_message(message.chat.id, "1. А.С.Пушкин\n2. А.А.Блок\n3. В.В.Маяквский", reply_markup=l2_2)
	elif message.text.lower() == 'основная информация о боте':
		bot.send_message(message.chat.id, "автор проекта: Никита Чесноков\nдата релиза: 1.08.2020\nВерсия: BETA 1", reply_markup=l2_2)
	#l2_3
	elif message.text.lower() == 'стихи пушкина':
		bot.send_message(message.chat.id, m.poems('Пушкин'), reply_markup=l2_2)
	elif message.text.lower() == 'стихи блока':
		bot.send_message(message.chat.id, m.poems('блок'), reply_markup=l2_2)
	elif message.text.lower() == 'стихи маяковского':
		bot.send_message(message.chat.id, m.poems('маяковский'), reply_markup=l2_2)
	#l2_2_1
	elif message.text.lower() == 'список стихов':
		bot.send_message(message.chat.id, 'список стихов какого автора вы хотите увидеть?', reply_markup=l2_3)
	#l3
	elif message.text.lower() == 'следующий стих пушкина':
		bot.send_message(message.chat.id, m.p_random(), reply_markup=l3_1)
	elif message.text.lower() == 'следующий стих блока':
		bot.send_message(message.chat.id, m.b_random(), reply_markup=l3_2)
	elif message.text.lower() == 'следующий стих маяковского':
		bot.send_message(message.chat.id, m.m_random(), reply_markup=l3_3)
	#all
	elif message.text.lower() == 'меню':
		bot.send_message(message.chat.id, "ok", reply_markup=main)

bot.polling()
