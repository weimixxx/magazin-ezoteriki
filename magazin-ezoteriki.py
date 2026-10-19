import time

from telebot.types import Message, InlineKeyboardMarkup, CallbackQuery, InlineKeyboardButton as IB
import random
import text
import telebot

bot = telebot.TeleBot("8571225589:AAGYoGXFltAJC3P21NorXUxcQ7anH05nuXM")

@bot.message_handler(["menu"])
def menu(msg:Message):
    kb = telebot.types.ReplyKeyboardMarkup(True, False)
    kb.row("Магический шар", "Книга «Гадаем на кофеиновой гуще»")
    kb.row("Хрустальный шар", "Руны")
    bot.send_message(msg.chat.id, text.menu, reply_markup=kb)
    bot.register_next_step_handler(msg, register_choice)



@bot.message_handler(["start"])
def start(msg:Message):
    kb = telebot.types.ReplyKeyboardMarkup(True, False)
    kb.row("Магический шар", "Книга «Гадаем на кофеиновой гуще»")
    kb.row("Хрустальный шар", "Руны")
    bot.send_message(msg.chat.id, text.start, reply_markup= kb)
    bot.register_next_step_handler(msg, register_choice)

def register_choice(msg: Message):
    if msg.text == "Магический шар":
        magic_square(msg)
    if msg.text == "Книга «Гадаем на кофейной гуще»":
        book_coffe(msg)
    if msg.text == "Хрустальный шар":
        glass_square(msg)
    if msg.text == "Руины":
        rune(msg)

def magic_square(msg: Message):
    bot.send_message(msg.chat.id, "Ты выбрал: магический шар! \nзадай ему какой нибудь вопрос!")
    bot.register_next_step_handler(msg, confirm, "magic_shar")

def book_coffe(msg: Message):
    gif = open("book-bfdia.gif", "rb")
    bot.send_document(msg.chat.id, gif, caption="Ты выбрал: Книга «Гадаем на кофейной гуще! \nзадай ему вопрос!")
    bot.register_next_step_handler(msg, confirm, "book_coffe")

def glass_square(msg: Message):
    kb2 = telebot.types.ReplyKeyboardMarkup()
    kb2.row("Случайное предсказание")

    kb1 = telebot.types.ReplyKeyboardMarkup()
    kb1.row("Случайное предсказание")
    kb1.row("Секретная предсказание(шанс 15%)")

    if random.randint(1, 100) <= 15:
        bot.send_message(msg.chat.id, "ты выбрал: Стклаянный шар\nОбратись к шару, то бы он заработал(нажми на кнопку)", reply_markup=kb1)
        bot.register_next_step_handler(msg, confirm, action = "glass_square1")
    else:
        bot.send_message(msg.chat.id, "ты выбрал: Стклаянный шар\nОбратись к шару, то бы он заработал(нажми на кнопку)", reply_markup=kb2)
        bot.register_next_step_handler(msg, confirm, action="glass_square2")

def rune(msg: Message):
    photo = open("img.png", "rb")
    kb = InlineKeyboardMarkup()
    kb.row(IB("Камень Ньютончика", callback_data=f"Newtone|{msg.from_user.username}"), IB("камень бейсика", callback_data=f"basik|{msg.from_user.username}"), IB("сила меньшего", callback_data=f"silla_nemshego|{msg.from_user.username}"))
    kb.row(IB("Камень икс", callback_data=f"sila_x|{msg.from_user.username}"), IB("камень моста", callback_data=f"most|{msg.from_user.username}"), IB("камень молний", callback_data=f'flash|{msg.from_user.username}'))
    bot.send_photo(msg.chat.id, photo ,caption="Ты выбрал Руны! \n Выбери свою руну для покупки и узнай правду о себе)", reply_markup=kb)


@bot.callback_query_handler(func = lambda call: True)
def calldata(call: CallbackQuery):
    if call.data.startswith("Newtone"):
        bot.send_message(call.message.chat.id, "Ты выбрал руну Ньютона! \nскоро с тобой свяжуться для обработки мелких деталей.")
        bot.send_message(2027005292, f'пользователь @{call.data.split("|")[1]} приобрел руну Ньютона')
    if call.data.startswith("basik"):
        bot.send_message(call.message.chat.id,"Ты выбрал руну Бейсика! \nскоро с тобой свяжуться для обработки мелких деталей.")
        bot.send_message(2027005292, f'пользователь @{call.data.split("|")[1]} приобрел руну Ньютона')
    if call.data.startswith("silla_nemshego"):
        bot.send_message(call.message.chat.id,
                         "Ты выбрал руну Меньшего! \nскоро с тобой свяжуться для обработки мелких деталей.")
        bot.send_message(2027005292, f'пользователь @{call.data.split("|")[1]} приобрел руну Ньютона')
    if call.data.startswith("sila_x"):
        bot.send_message(call.message.chat.id,
                         "Ты выбрал руну Икса! \nскоро с тобой свяжуться для обработки мелких деталей.")
        bot.send_message(2027005292, f'пользователь @{call.data.split("|")[1]} приобрел руну Ньютона')
    if call.data.startswith("most"):
        bot.send_message(call.message.chat.id,
                         "Ты выбрал руну моста! \nскоро с тобой свяжуться для обработки мелких деталей.")
        bot.send_message(2027005292, f'пользователь @{call.data.split("|")[1]} приобрел руну Ньютона')
    if call.data.startswith("flash"):
        bot.send_message(call.message.chat.id,
                         "Ты выбрал руну молния! \nскоро с тобой свяжуться для обработки мелких деталей.")
        bot.send_message(2027005292, f'пользователь @{call.data.split("|")[1]} приобрел руну Ньютона')


def confirm(msg:Message, action):
    kb_yes_no = telebot.types.ReplyKeyboardMarkup()
    kb_yes_no.row("да", "нет")
    if  action == "magic_shar":
        list_slov = random.choice(text.magic_square_list)
        bot.send_message(msg.chat.id, f"Магический шар отвечает: {list_slov}")
        time.sleep(2)
        menu(msg)

    if action == "book_coffe":
        list_slov = random.choice(text.book_coffe_list)
        bot.send_message(msg.chat.id,  list_slov)
        menu(msg)


    if action == "glass_square1":
        gif = open("dearh_poverty.gif", "rb")

        if msg.text =="Случайное предсказание":
            slov1 =random.choice(["вам","тебе"])
            slov2 = random.choice(["завтра","через год","сегодня","в будущем", "через пару часов", "через месяц", f"через {random.randint(1,24)} часа(ов)"])
            slov3 = random.choice(["найдешь 5 миллион рублей","встретишься с кумиром","испугаешься","увидишь произшествие", "расстанешься", "сойдешься", "пропадешь", "надйешь работу", "скажет ганвест пепе", "станешь популярным"])
            bot.send_message(msg.chat.id, f"{slov1} {slov2} {slov3}")
            menu(msg)

        if msg.text == "Секретная предсказание(шанс 10%)":
            bot.send_document(msg.chat.id, gif, caption="это твоё будущее")
            time.sleep(3)
            menu(msg)

    if action == "glass_square2":
        slov1 = random.choice(["ты", "тебе"])
        slov2 = random.choice(["завтра", "через год", "сегодня", "в будущем", "через пару часов", "через месяц", f"через {random.randint(1, 24)} часа(ов)"])
        slov3 = random.choice(["найдешь 1 миллион рублей", "встретишься с кумиром", "испугаешься", "увидишь произшествие", "расстанешься", "сойдешься", "пропадешь", "надйешь работу", "скажет ганвест пепе", "станешь популярным"])
        bot.send_message(msg.chat.id, f"{slov1} {slov2} {slov3}")
        menu(msg)



bot.infinity_polling()