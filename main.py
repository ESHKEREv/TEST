import telebot
from telebot import types



bot = telebot.TeleBot('5942659248:AAFxSwUV1RWHk26k6f7TQJBIsFtLeTnb0wU')



@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет!, {message.from_user.first_name} , этот бот даст тебе возможность пройти тэст по основам пайтон. Если ты готов напиши <u><b>Поехали</b></u>', parse_mode = 'html')



@bot.message_handler()
def info(message):
    score = 0
    quetions = [f'итак, {message.from_user.first_name} ,этот тэст будет состоять из 30 вопросов. По окончанию тэста ты узнаеши свой результат.Вот твой первый вопрос - Сколько библиотек можно импортировать в один проект?','Команда input() используется для?','Python это компилятор или интерпретатор?','Какиая встроенные структура данных существуют в python?','Какая функция используется для ввода информации в Python?','Какая функция используется для вывода информации в Python?']
    if message.text.lower() == 'поехали':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('3')
        btn2 = types.KeyboardButton('4')
        btn3 = types.KeyboardButton('6')
        btn4 = types.KeyboardButton('неограниченое количество')
        markup.row(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id,quetions[0],parse_mode='html',reply_markup=markup)
    if message.chat.type == 'private':

        if message.text == 'неограниченое количество':
            score += 1
            markup_2 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('считывания данных с клавиатуры')
            btn2 = types.KeyboardButton('вывода данных на экран')
            markup_2.row(btn1, btn2)
            bot.send_message(message.chat.id,quetions[1] ,reply_markup=markup_2)
        elif message.text == '3':
            markup_2 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('считывания данных с клавиатуры')
            btn2 = types.KeyboardButton('вывода данных на экран')
            markup_2.row(btn1, btn2)
            bot.send_message(message.chat.id, quetions[1], reply_markup=markup_2)
        elif message.text == '4':
            markup_2 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('считывания данных с клавиатуры')
            btn2 = types.KeyboardButton('вывода данных на экран')
            markup_2.row(btn1, btn2)
            bot.send_message(message.chat.id, quetions[1], reply_markup=markup_2)
        elif message.text == '6':
            markup_2 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('считывания данных с клавиатуры')
            btn2 = types.KeyboardButton('вывода данных на экран')
            markup_2.row(btn1, btn2)
            bot.send_message(message.chat.id, quetions[1], reply_markup=markup_2)

        if message.text == 'считывания данных с клавиатуры':
            score += 1
            markup_3 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('компилятор')
            btn2 = types.KeyboardButton('интерпретатор')
            markup_3.row(btn1, btn2)
            bot.send_message(message.chat.id, quetions[2],reply_markup=markup_3)
        elif message.text == 'вывода данных на экран':
            markup_3 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('компилятор')
            btn2 = types.KeyboardButton('интерпретатор')
            markup_3.row(btn1, btn2)
            bot.send_message(message.chat.id, quetions[2], reply_markup=markup_3)

        if message.text == 'интерпретатор':
            score += 1
            markup_4 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('frozenset')
            btn2 = types.KeyboardButton('list')
            btn3 = types.KeyboardButton('map')
            btn4 = types.KeyboardButton('array')
            markup_4.row(btn1, btn2, btn3, btn4)
            bot.send_message(message.chat.id, quetions[3], reply_markup=markup_4)
        elif message.text == 'компилятор':
            markup_4 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('frozenset')
            btn2 = types.KeyboardButton('list')
            btn3 = types.KeyboardButton('map')
            btn4 = types.KeyboardButton('array')
            markup_4.row(btn1, btn2, btn3, btn4)
            bot.send_message(message.chat.id, quetions[3], reply_markup=markup_4)

        if message.text == 'frozenset':
            score += 1
            markup_5 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('88')
            btn2 = types.KeyboardButton('64')
            btn3 = types.KeyboardButton('8')
            btn4 = types.KeyboardButton('88888888')
            markup_5.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_4.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_5)
        elif message.text == 'list':
            score += 1
            markup_5 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('88')
            btn2 = types.KeyboardButton('64')
            btn3 = types.KeyboardButton('8')
            btn4 = types.KeyboardButton('88888888')
            markup_5.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_4.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_5)
        elif message.text == 'map':
            score += 1
            markup_5 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('88')
            btn2 = types.KeyboardButton('64')
            btn3 = types.KeyboardButton('8')
            btn4 = types.KeyboardButton('88888888')
            markup_5.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_4.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_5)
        elif message.text == 'array':
            markup_5 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('88')
            btn2 = types.KeyboardButton('64')
            btn3 = types.KeyboardButton('8')
            btn4 = types.KeyboardButton('88888888')
            markup_5.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_4.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_5)

        if message.text == '88':
            markup_6 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('TypeError')
            btn2 = types.KeyboardButton('-4')
            btn3 = types.KeyboardButton('9')
            btn4 = types.KeyboardButton('4')
            markup_6.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_5.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_6)
        elif message.text == '64':
            markup_6 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('TypeError')
            btn2 = types.KeyboardButton('-4')
            btn3 = types.KeyboardButton('9')
            btn4 = types.KeyboardButton('4')
            markup_6.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_5.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_6)
        elif message.text == '8':
            markup_6 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('TypeError')
            btn2 = types.KeyboardButton('-4')
            btn3 = types.KeyboardButton('9')
            btn4 = types.KeyboardButton('4')
            markup_6.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_5.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_6)
        elif message.text == '88888888':
            score += 1
            markup_6 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('TypeError')
            btn2 = types.KeyboardButton('-4')
            btn3 = types.KeyboardButton('9')
            btn4 = types.KeyboardButton('4')
            markup_6.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_5.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_6)

        if message.text == 'TypeError':
            markup_7 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("'2'")
            btn2 = types.KeyboardButton("'4'")
            btn3 = types.KeyboardButton('2.0')
            btn4 = types.KeyboardButton('4.0')
            markup_7.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_6.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_7)
        elif message.text == '-4':
            markup_7 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("'2'")
            btn2 = types.KeyboardButton("'4'")
            btn3 = types.KeyboardButton('2.0')
            btn4 = types.KeyboardButton('4.0')
            markup_7.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_6.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_7)
        elif message.text == '9':
            score += 1
            markup_7 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("'2'")
            btn2 = types.KeyboardButton("'4'")
            btn3 = types.KeyboardButton('2.0')
            btn4 = types.KeyboardButton('4.0')
            markup_7.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_6.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_7)
        elif message.text == '4':
            markup_7 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("'2'")
            btn2 = types.KeyboardButton("'4'")
            btn3 = types.KeyboardButton('2.0')
            btn4 = types.KeyboardButton('4.0')
            markup_7.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_6.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_7)

        if message.text == "'2'":
            score += 1
            markup_8 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('Привет > мир')
            btn2 = types.KeyboardButton('Привет < мир')
            btn3 = types.KeyboardButton('True')
            btn4 = types.KeyboardButton('False')
            markup_8.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_7.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_8)
        elif message.text == "'4'":
            markup_8 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('Привет > мир')
            btn2 = types.KeyboardButton('Привет < мир')
            btn3 = types.KeyboardButton('True')
            btn4 = types.KeyboardButton('False')
            markup_8.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_7.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_8)
        elif message.text == '2.0':
            markup_8 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('Привет > мир')
            btn2 = types.KeyboardButton('Привет < мир')
            btn3 = types.KeyboardButton('True')
            btn4 = types.KeyboardButton('False')
            markup_8.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_7.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_8)
        elif message.text == '4.0':
            markup_8 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('Привет > мир')
            btn2 = types.KeyboardButton('Привет < мир')
            btn3 = types.KeyboardButton('True')
            btn4 = types.KeyboardButton('False')
            markup_8.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_7.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_8)

        if message.text == 'Привет > мир':
            markup_9 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("'-}-:-]-'")
            btn2 = types.KeyboardButton("}:', ']', '-")
            btn3 = types.KeyboardButton("'}:', ']', sep='-'")
            btn4 = types.KeyboardButton('}:-]')
            markup_9.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_8.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_9)
        elif message.text == 'Привет < мир':
            markup_9 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("'-}-:-]-'")
            btn2 = types.KeyboardButton("}:', ']', '-")
            btn3 = types.KeyboardButton("'}:', ']', sep='-'")
            btn4 = types.KeyboardButton('}:-]')
            markup_9.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_8.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_9)
        elif message.text == 'True':
            markup_9 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("'-}-:-]-'")
            btn2 = types.KeyboardButton("}:', ']', '-")
            btn3 = types.KeyboardButton("'}:', ']', sep='-'")
            btn4 = types.KeyboardButton('}:-]')
            markup_9.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_8.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_9)
        elif message.text == 'False':
            score += 1
            markup_9 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("'-}-:-]-'")
            btn2 = types.KeyboardButton("}:', ']', '-")
            btn3 = types.KeyboardButton("'}:', ']', sep='-'")
            btn4 = types.KeyboardButton('}:-]')
            markup_9.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_8.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_9)

        if message.text == "'-}-:-]-'":
            markup_10 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("9450")
            btn2 = types.KeyboardButton("9540")
            btn3 = types.KeyboardButton("5940")
            btn4 = types.KeyboardButton("'0'")
            markup_10.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_9.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_10)
        elif message.text == "}:', ']', '-":
            markup_10 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("9450")
            btn2 = types.KeyboardButton("9540")
            btn3 = types.KeyboardButton("5940")
            btn4 = types.KeyboardButton("'0'")
            markup_10.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_9.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_10)
        elif message.text == "'}:', ']', sep='-'":
            markup_10 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("9450")
            btn2 = types.KeyboardButton("9540")
            btn3 = types.KeyboardButton("5940")
            btn4 = types.KeyboardButton("'0'")
            markup_10.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_9.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_10)
        elif message.text == '}:-]':
            score += 1
            markup_10 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("9450")
            btn2 = types.KeyboardButton("9540")
            btn3 = types.KeyboardButton("5940")
            btn4 = types.KeyboardButton("'0'")
            markup_10.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_9.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_10)

        if message.text == "9450":
            score += 1
            markup_11 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("'False'")
            btn2 = types.KeyboardButton("TypeError")
            btn3 = types.KeyboardButton("SyntaxError")
            btn4 = types.KeyboardButton('0')
            markup_11.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_10.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_11)
        elif message.text == "9540":
            markup_11 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("'False'")
            btn2 = types.KeyboardButton("TypeError")
            btn3 = types.KeyboardButton("SyntaxError")
            btn4 = types.KeyboardButton('0')
            markup_11.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_10.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_11)
        elif message.text == "5940'":
            markup_11 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("'False'")
            btn2 = types.KeyboardButton("TypeError")
            btn3 = types.KeyboardButton("SyntaxError")
            btn4 = types.KeyboardButton('0')
            markup_11.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_10.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_11)
        elif message.text == "'0'":
            score += 1
            markup_11 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("'False'")
            btn2 = types.KeyboardButton("TypeError")
            btn3 = types.KeyboardButton("SyntaxError")
            btn4 = types.KeyboardButton('0')
            markup_11.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_10.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_11)

        if message.text == "'False'":
            markup_12 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("Truе")
            btn2 = types.KeyboardButton("Falsе")
            btn3 = types.KeyboardButton("SyntxError")
            btn4 = types.KeyboardButton('TypeError')
            markup_12.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_11.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_12)
        elif message.text == "TypeError":
            score += 1
            markup_12 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("True")
            btn2 = types.KeyboardButton("False")
            btn3 = types.KeyboardButton("SyntaxError")
            btn4 = types.KeyboardButton('TypeError')
            markup_12.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_11.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_12)
        elif message.text == "SyntaxError":
            markup_12 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("True")
            btn2 = types.KeyboardButton("False")
            btn3 = types.KeyboardButton("SyntaxError")
            btn4 = types.KeyboardButton('TypeError')
            markup_12.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_11.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_12)
        elif message.text == '0':
            markup_12 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("True")
            btn2 = types.KeyboardButton("False")
            btn3 = types.KeyboardButton("SyntaxError")
            btn4 = types.KeyboardButton('TypeError')
            markup_12.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_11.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_12)

        if message.text == "'True'":
            markup_13 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("Ну конечно же! Ну теперь-то я уверен.")
            btn2 = types.KeyboardButton("Или нет?")
            btn3 = types.KeyboardButton("Ну конечно же! Наверняка!")
            btn4 = types.KeyboardButton('Ну конечно же! Наверняка! Ну теперь-то я уверен.')
            markup_13.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_12.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_13)
        elif message.text == "False":
            score += 1
            markup_13 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("Ну конечно же! Ну теперь-то я уверен.")
            btn2 = types.KeyboardButton("Или нет?")
            btn3 = types.KeyboardButton("Ну конечно же! Наверняка!")
            btn4 = types.KeyboardButton('Ну конечно же! Наверняка! Ну теперь-то я уверен.')
            markup_13.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_12.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_13)
        elif message.text == "SyntaxError":
            markup_13 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("Ну конечно же! Ну теперь-то я уверен.")
            btn2 = types.KeyboardButton("Или нет?")
            btn3 = types.KeyboardButton("Ну конечно же! Наверняка!")
            btn4 = types.KeyboardButton('Ну конечно же! Наверняка! Ну теперь-то я уверен.')
            markup_13.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_12.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_13)
        elif message.text == 'TypeError':
            markup_13 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("Ну конечно же! Ну теперь-то я уверен.")
            btn2 = types.KeyboardButton("Или нет?")
            btn3 = types.KeyboardButton("Ну конечно же! Наверняка!")
            btn4 = types.KeyboardButton('Ну конечно же! Наверняка! Ну теперь-то я уверен.')
            markup_13.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_12.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_13)

        if message.text == "Ну конечно же! Ну теперь-то я уверен.":
            score += 1
            markup_15 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("Внимание")
            btn2 = types.KeyboardButton("Старт")
            btn3 = types.KeyboardButton("Перерыв")
            btn4 = types.KeyboardButton('Финал')
            markup_15.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_13.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_15)
        elif message.text == "Или нет?":
            markup_15 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("Внимание")
            btn2 = types.KeyboardButton("Старт")
            btn3 = types.KeyboardButton("Перерыв")
            btn4 = types.KeyboardButton('Финал')
            markup_15.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_13.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_15)
        elif message.text == "Ну конечно же! Наверняка!":
            markup_15 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("Внимание")
            btn2 = types.KeyboardButton("Старт")
            btn3 = types.KeyboardButton("Перерыв")
            btn4 = types.KeyboardButton('Финал')
            markup_15.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_13.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_15)
        elif message.text == 'Ну конечно же! Наверняка! Ну теперь-то я уверен.':
            markup_15 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("Внимание")
            btn2 = types.KeyboardButton("Старт")
            btn3 = types.KeyboardButton("Перерыв")
            btn4 = types.KeyboardButton('Финал')
            markup_15.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_13.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_15)

        if message.text == "Внимание":
            markup_16 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("20")
            btn2 = types.KeyboardButton("1")
            btn3 = types.KeyboardButton("2")
            btn4 = types.KeyboardButton('18')
            markup_16.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_14.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_16)
        elif message.text == "Старт":
            markup_16 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("20")
            btn2 = types.KeyboardButton("1")
            btn3 = types.KeyboardButton("2")
            btn4 = types.KeyboardButton('18')
            markup_16.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_14.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_16)
        elif message.text == "Перерыв":
            markup_16 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("20")
            btn2 = types.KeyboardButton("1")
            btn3 = types.KeyboardButton("2")
            btn4 = types.KeyboardButton('18')
            markup_16.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_14.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_16)
        elif message.text == 'Финал':
            score += 1
            markup_16 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("20")
            btn2 = types.KeyboardButton("1")
            btn3 = types.KeyboardButton("2")
            btn4 = types.KeyboardButton('18')
            markup_16.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_14.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_16)

        if message.text == "20":
            score += 1
            markup_17 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("Ничего")
            btn2 = types.KeyboardButton("Удалить [1]")
            btn3 = types.KeyboardButton("Заменить ф-ю min на max")
            markup_17.row(btn1, btn2, btn3)
            file = open('./quetion_15.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_17)
        elif message.text == "1":
            markup_17 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("Ничего")
            btn2 = types.KeyboardButton("Удалить [1]")
            btn3 = types.KeyboardButton("Заменить ф-ю min на max")
            markup_17.row(btn1, btn2, btn3)
            file = open('./quetion_15.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_17)
        elif message.text == "2":
            markup_17 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("Ничего")
            btn2 = types.KeyboardButton("Удалить [1]")
            btn3 = types.KeyboardButton("Заменить ф-ю min на max")
            markup_17.row(btn1, btn2, btn3)
            file = open('./quetion_15.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_17)
        elif message.text == '18':
            markup_17 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("Ничего")
            btn2 = types.KeyboardButton("Удалить [1]")
            btn3 = types.KeyboardButton("Заменить ф-ю min на max")
            markup_17.row(btn1, btn2, btn3)
            file = open('./quetion_15.png', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_17)

        if message.text == "Ничего":
            markup_18 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("int()")
            btn2 = types.KeyboardButton("input()")
            btn3 = types.KeyboardButton("print()")
            btn4 = types.KeyboardButton("str()")
            markup_18.row(btn1, btn2, btn3, btn4)
            bot.send_message(message.chat.id, quetions[4], reply_markup=markup_18)
        elif message.text == "Удалить [1]":
            score += 1
            markup_18 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("int()")
            btn2 = types.KeyboardButton("input()")
            btn3 = types.KeyboardButton("print()")
            btn4 = types.KeyboardButton("str()")
            markup_18.row(btn1, btn2, btn3, btn4)
            bot.send_message(message.chat.id, quetions[4], reply_markup=markup_18)
        elif message.text == 'Заменить ф-ю min на max':
            markup_18 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("int()")
            btn2 = types.KeyboardButton("input()")
            btn3 = types.KeyboardButton("print()")
            btn4 = types.KeyboardButton("str()")
            markup_18.row(btn1, btn2, btn3, btn4)
            bot.send_message(message.chat.id, quetions[4], reply_markup=markup_18)

        if message.text == "int()":
            markup_19 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("[2]")
            btn2 = types.KeyboardButton("[1,1]")
            btn3 = types.KeyboardButton("[11]")
            btn4 = types.KeyboardButton("Ошибку")
            markup_19.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_16.PNG', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_19)
        elif message.text == "input()":
            score += 1
            markup_19 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("[2]")
            btn2 = types.KeyboardButton("[1,1]")
            btn3 = types.KeyboardButton("[11]")
            btn4 = types.KeyboardButton("Ошибку")
            markup_19.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_16.PNG', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_19)
        elif message.text == 'print()':
            markup_19 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("[2]")
            btn2 = types.KeyboardButton("[1,1]")
            btn3 = types.KeyboardButton("[11]")
            btn4 = types.KeyboardButton("Ошибку")
            markup_19.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_16.PNG', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_19)
        elif message.text == 'str()':
            markup_19 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("[2]")
            btn2 = types.KeyboardButton("[1,1]")
            btn3 = types.KeyboardButton("[11]")
            btn4 = types.KeyboardButton("Ошибку")
            markup_19.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_16.PNG', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_19)
        if message.text == "int()":
            markup_19 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("[2]")
            btn2 = types.KeyboardButton("[1,1]")
            btn3 = types.KeyboardButton("[11]")
            btn4 = types.KeyboardButton("Ошибку")
            markup_19.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_16.PNG', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_19)
        elif message.text == "input()":
            score += 1
            markup_19 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("[2]")
            btn2 = types.KeyboardButton("[1,1]")
            btn3 = types.KeyboardButton("[11]")
            btn4 = types.KeyboardButton("Ошибку")
            markup_19.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_16.PNG', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_19)
        elif message.text == 'print()':
            markup_19 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("[2]")
            btn2 = types.KeyboardButton("[1,1]")
            btn3 = types.KeyboardButton("[11]")
            btn4 = types.KeyboardButton("Ошибку")
            markup_19.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_16.PNG', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_19)
        elif message.text == 'str()':
            markup_19 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("[2]")
            btn2 = types.KeyboardButton("[1,1]")
            btn3 = types.KeyboardButton("[11]")
            btn4 = types.KeyboardButton("Ошибку")
            markup_19.row(btn1, btn2, btn3, btn4)
            file = open('./quetion_16.PNG', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_19)

        if message.text == "[2]":
            markup_20 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("hheelllloo wwoorrlldd")
            btn2 = types.KeyboardButton("hheelloo wwoorrlldd")
            btn3 = types.KeyboardButton("hello world")
            markup_20.row(btn1, btn2, btn3)
            file = open('./quetion_16.PNG', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_20)
        elif message.text == "[1,1]":
            score += 1
            markup_20 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("hheelllloo wwoorrlldd")
            btn2 = types.KeyboardButton("hheelloo wwoorrlldd")
            btn3 = types.KeyboardButton("hello world")
            markup_20.row(btn1, btn2, btn3)
            file = open('./quetion_16.PNG', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_20)
        elif message.text == '[11]':
            markup_20 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("hheelllloo wwoorrlldd")
            btn2 = types.KeyboardButton("hheelloo wwoorrlldd")
            btn3 = types.KeyboardButton("hello world")
            markup_20.row(btn1, btn2, btn3)
            file = open('./quetion_16.PNG', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_20)
        elif message.text == 'Ошибку':
            markup_20 = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton("hheelllloo wwoorrlldd")
            btn2 = types.KeyboardButton("hheelloo wwoorrlldd")
            btn3 = types.KeyboardButton("hello world")
            markup_20.row(btn1, btn2, btn3)
            file = open('./quetion_16.PNG', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup_20)

        # этот участок кода, кажется, связан с ответами, но он не завершен!!!!!!
        # пожалуйста, укажи еще отсутствующий текст, который должен быть отправлен в качестве сообщения

        if message.text == "hheelloo wwoorrlldd":
            bot.send_message(message.chat.id, 'Молодец! Ты прошел тест. Вот твой результат:', score)
        elif message.text == "hheelllloo wwoorrlldd":
            score += 1
            bot.send_message(message.chat.id, 'Молодец! Ты прошел тест. Вот твой результат:', score)
        elif message.text == "hello world":
            score += 1
            bot.send_message(message.chat.id, 'Молодец! Ты прошел тест. Вот твой результат:', score)




bot.polling(none_stop=True)