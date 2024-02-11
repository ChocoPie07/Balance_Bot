import telebot
from telebot import types

botTimeWeb = telebot.TeleBot('6890974387:AAFcw5vcr5tyIpj2SP4qXOT0vJGX0Gr7SkQ')

@botTimeWeb.message_handler(commands=['start'])
def startBot(message):
    first_mess = f"<b>{message.from_user.first_name}</b>, привет!\nХочешь расскажу немного о тебе?"
    markup = types.InlineKeyboardMarkup()

    button_fun = types.InlineKeyboardButton(text='Функционал', callback_data='fun')
    button_lk = types.InlineKeyboardButton(text='ЛК', callback_data='LK')
    button_fantasy = types.InlineKeyboardButton(text='Фантазерство', callback_data='fantasy')
    button_about = types.InlineKeyboardButton(text='О нас', callback_data='about')

    markup.add(button_fun, button_lk)
    markup.add(button_fantasy, button_about)

    botTimeWeb.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)

@botTimeWeb.callback_query_handler(func=lambda call: True)
def response(function_call):
    if function_call.message:
        if function_call.data == "fun":
            second_mess = "Доступный на данный момент функционал:"
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Прогноз на сегодня", callback_data='forecast'))
            markup.add(types.InlineKeyboardButton("Функция2", callback_data='forecast'))
            markup.add(types.InlineKeyboardButton("Функция3", callback_data='forecast'))
            botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
            botTimeWeb.answer_callback_query(function_call.id)
        elif function_call.data == "LK":
            first_text = "О вас:"
            botTimeWeb.send_message(function_call.message.chat.id, first_text)
            # Используйте function_call.message.chat.id вместо chat_id
            chat_id = function_call.message.chat.id
            botTimeWeb.send_photo(chat_id, open('C:\\Users\\Сулейман\\pythonProject\\ИС\\Дракон козерог.png', 'rb'))
            second_mess = "Фамилия: Иванов\nИмя: Иван\nОтчество: Иванович\nДата рождения: 1.1.1970\nВозраст: 54\nЗЗ: Козерог\nПланета: Сатурн\nДеканат: Венера\nИ так далее..."
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Изменить данные", callback_data='name'))
            botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
            botTimeWeb.answer_callback_query(function_call.id)
        elif function_call.data == "fantasy":
            second_mess = "Можете преобрести:"
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("План на день", callback_data='plan'))
            markup.add(types.InlineKeyboardButton("Натальная карта", callback_data='natal_chart'))
            markup.add(types.InlineKeyboardButton("Общение с нашим экспертом", callback_data='communication'))
            botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
            botTimeWeb.answer_callback_query(function_call.id)
        elif function_call.data == "about":
            second_mess = "О нас:"
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Чат", url='https://t.me/+iObuNN1CIDY1NDMy'))
            markup.add(types.InlineKeyboardButton("Канал", url='https://t.me/+JmMtrsm1gK4yMDIy'))
            botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
            botTimeWeb.answer_callback_query(function_call.id)

botTimeWeb.infinity_polling()
