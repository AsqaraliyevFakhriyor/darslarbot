import telebot
# from telebot import types
from keyboarddata import *
import sqlite3
from models import dars
from time import sleep

file_id = "a"
db = sqlite3.connect('bot_users.db', check_same_thread=False)
sql = db.cursor()
# sqlite3.connect(":memory:", check_same_thread=False)

sql.execute('''CREATE TABLE IF NOT EXISTS bot_users(
        name VARCHAR,
        user_id VARCHAR)''')

TOKEN = "TELEGRAM BOT TOKEN"
bot = telebot.TeleBot(TOKEN)

""" simple animation function """
def download_animation(message):
    try:
        bot.send_message(message.chat.id, '🕛')
        bot.edit_message_text(chat_id=message.chat.id, message_id=int(message.message_id) + 1, text='🕓')
        bot.edit_message_text(chat_id=message.chat.id, message_id=int(message.message_id) + 1, text='🕗')
        bot.edit_message_text(chat_id=message.chat.id, message_id=int(message.message_id) + 1, text='☑')
        sleep(0.2)
        bot.delete_message(chat_id=message.chat.id, message_id=int(message.message_id) + 1, timeout=0)
    except:
        pass
        # bot.send_message(message.chat.id, '😕 Tizimda nosozlik \n♻️ Qaytadan urinib ko`ring')



""" Message Handlers """
@bot.message_handler(commands=['start'])
def start(message):

    # you can force user to join your telegram channel, if he wants to use your bot sevice!
    a = bot.get_chat_member('YOUR TELEGRAM CHANNEL', message.from_user.id)
    allowed_list = ['member', 'administrator', 'creator', 'left']

    user_id = message.from_user.id
    if message.from_user.username:
        name = '@' + message.chat.username
    else:
        name = "noname"
    if True:

        """ if user not exist, inserting data to database  """
        if sql.execute(f"SELECT user_id FROM bot_users WHERE user_id = ?", (user_id,)).fetchall() != []:
            last_name = ((sql.execute(f"SELECT name FROM bot_users WHERE user_id = ?", (user_id,))).fetchone())[0]
            sql.execute(f"UPDATE bot_users SET name = ? WHERE name = ?", (name, last_name))
            db.commit()

        elif sql.execute(f"SELECT user_id FROM bot_users WHERE user_id = ?", (user_id,)).fetchall() == []:
            sql.execute("INSERT INTO bot_users VALUES(?,?)", (name, user_id))
            db.commit()


        markup_n1 = types.ReplyKeyboardMarkup(row_width=2)
        markup_n1.add(istem_1, item2, item3, item4, item5, item6)

        bot.send_message(message.chat.id,
                         "\n🙋‍Asalomu aleykum \'<b>{0.first_name}\'</b> "
                         "\n_________________________________________"
                         "\n👨🏻‍💻 <b><u>{1.first_name}</u></b>ga xush kelibsiz "
                         "\n_________________________________________"
                         "\nBu yerda siz har xil sohalarda video "
                         "\ndarsliklar va amaliy mashg'ulotlar topa \nolasiz"
                         "\n_________________________________________"
                         "\n🤖Botga kundan kun yangi darslar\n joylanmoqda🙂"
                         "\n_________________________________________"
                         "\n‼️<i>Hozirda bizda IT dasturlash tillaridan</i>"
                         "\n<i>faqat</i> <b>Python  🐍, HTML</b>, <b>PHP</b>  \n va <b>pythonda telegrambot yasash</b>\n<i>darslari mavjud</i>"
                         "\n_________________________________________"
                         "\n ♻️Tez kinlarda yangi darslarniham \nqo'shishga harakat qilamiz🤓"
                         "\n_________________________________________"
                         "\nBot to'g'risida kamchiliklar, taklif va \ntafsiyalaringiz bo'lsa"
                         "\n --YOUR USERNAME-- ga yozishingizni \nso'rab qolamiz 😊"
                         "\n_________________________________________"
                         "\nDO'STALRINGIZ BILAN ULASHING "
                         "\n<b>LINK</b>: <i>@on_line_darslarbot</i>"
                         "\n_________________________________________".format(
                             message.from_user, bot.get_me()), reply_markup=markup_n1, parse_mode='html')



@bot.message_handler(commands=['home'])
def home(message):
    a = bot.get_chat_member('@music_region_songs_ncs_spotify', message.from_user.id)
    allowed_list = ['member', 'administrator', 'creator']
    if True:
        bot.send_message(message.chat.id, '🕛')
        markup_n1 = types.ReplyKeyboardMarkup(row_width=2)
        markup_n1.add(istem_1, item2, item3, item4, item5, item6)
        bot.edit_message_text(chat_id=message.chat.id, message_id=int(message.message_id)+1, text='🕓')
        bot.edit_message_text(chat_id=message.chat.id, message_id=int(message.message_id) + 1, text='🕗')
        bot.edit_message_text(chat_id=message.chat.id, message_id=int(message.message_id)+1, text='🔙')
        sleep(0.25)
        bot.delete_message(chat_id=message.chat.id, message_id=int(message.message_id) + 1, timeout=0)
        bot.send_message(message.chat.id, "Bosh Menu 📱", reply_markup=markup_n1)

@bot.message_handler(func=lambda message: True)
def keyboards_func(message):
            # sections
    if message.text == 'IT Dasturlash 💻':
        it_second_menu = types.ReplyKeyboardMarkup(row_width=2)
        it_second_menu.add(item1, html, css, javascrip, python, php, java, cplusplus, android, gamedev,telebot_python,
                           it_kod_editorlar)
        download_animation(message)
        bot.send_message(message.chat.id, "Dasturlash menusi📲", reply_markup=it_second_menu)

            # def programming languasges
        # python
    elif message.text == 'Python 🐍':
        it_python = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
        it_python.add(item1, python_sariq_dev)
        download_animation(message)
        bot.send_message(message.chat.id,"Python Darslar     📗 \nUlarning aftorlari  👨🏻‍🏫 \nYouTube Kanallar 📺"
                                         , reply_markup=it_python)

        # def html


            # def teachers

    elif message.text == "Narzullayev Anvar(YouTube: SariqDEV)":
        it_python_sariq_menu = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        it_python_sariq_menu.add(item1, python_sariq_dev_360, python_sariq_dev_720)
        download_animation(message)
        bot.send_message(message.chat.id, "Python Darslar     📗 \nHar xil sifatlarda (o'lchamlarham farq qiladi)"
                         , reply_markup=it_python_sariq_menu)

    elif message.text == "Darslar(360p)":
        python_courses = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=False)
        python_courses.add(item1, sariqdev_dars_boshi, sariqdev_kirish, sariqdev1, sariqdev2, sariqdev3, sariqdev4,
                           sariqdev5, sariqdev6, sariqdev7, sariqdev8, sariqdev9, sariqdev10,sariqdev11,
                           sariqdev12, sariqdev13, sariqdev14, sariqdev15, sariqdev16, sariqdev17, sariqdev18,
                           sariqdev19, sariqdev20, sariqdev21, sariqdev22,sariqdev23, sariqdev24, sariqdev25, sariqdev26
                           , sariqdev27,sariqdev28_1, sariqdev28, sariqdev29, sariqdev30, sariqdev31, sariqdev32, sariqdev33,
                           sariqdev34, sariqdev35, sariqdev36, sariqdev37, sariqdev38, sariqdev39, sariqdev40)
        download_animation(message)
        msgs = bot.send_message(message.chat.id, "Darslar bo'limi(360p) 📚", reply_markup=python_courses)
        bot.register_next_step_handler(msgs, darslar_python)

    elif message.text == "Darslar(720p(HD))":
        python_courses = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=False)
        python_courses.add(item1, sariq_dev0, sariq_dev01, sariq_dev1, sariq_dev2,sariq_dev3, sariq_dev4, sariq_dev5,
                           sariq_dev6,sariq_dev7, sariq_dev8, sariq_dev9,sariqdev10, sariq_dev11, sariq_dev12,
                           sariqdev13, sariq_dev13, sariqdev14, sariq_dev15, sariq_dev16, sariq_dev17, sariq_dev18,
                           sariq_dev19, sariq_dev20, sariq_dev21, sariq_dev22, sariq_dev23, sariq_dev24,
                           sariq_dev25, sariq_dev26, sariq_dev27, sariq_dev28, sariq_dev282, sariq_dev29,
                           sariq_dev30, sariq_dev31, sariq_dev32, sariq_dev33, sariq_dev34, sariq_dev35, sariq_dev36,
                           sariq_dev37, sariq_dev38, sariq_dev39, sariq_dev40)
        download_animation(message)
        msgs = bot.send_message(message.chat.id, "Darslar bo'limi(720p(HD)) 📚", reply_markup=python_courses)
        bot.register_next_step_handler(msgs, darslar_python)
# html menu
    elif message.text == 'HTML':
        it_html = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        it_html.add(item1, webbrain_html)
        download_animation(message)
        bot.send_message(message.chat.id, "HTML darslari \n Darslarning Aftorlari \nYouTube Kanallar 📺"
                         , reply_markup=it_html)
# webbrain html menu
    elif message.text == "WebBrain Academy (YT: Web Brain Academy)":
        it_html_webbrain = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        it_html_webbrain.add(item1, webrain_lesson_html, webrain_lesson1_html, webrain_lesson2_html,
                             webrain_lesson3_html, webrain_lesson5_html, webrain_lesson6_html,
                             webrain_lesson7_html, webrain_lesson8_html, webrain_lesson9_html,
                             webrain_lesson10_html, webrain_lesson11_html, webrain_alllesson_html)

        download_animation(message)
        msg = bot.send_message(message.chat.id, "Darslar bo'limi 📚"
                         , reply_markup=it_html_webbrain)
        bot.register_next_step_handler(msg, darslar_python)
# PHP menu
    elif message.text == 'PHP':
        it_php = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        it_php.add(item1, programmeruz_php)
        download_animation(message)
        bot.send_message(message.chat.id, "PHP darslari \n Darslarning Aftorlari \nYouTube Kanallar 📺"
                         , reply_markup=it_php)
    # webbrain html menu
    elif message.text == "Programmers Uz (YT: Programmer_uz)":
        it_php_programmeruz = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        it_php_programmeruz.add(item1, programmeruzphp1_lesson, programmeruzphp2_lesson, programmeruzphp3_lesson,
                                programmeruzphp4_lesson, programmeruzphp5_lesson, programmeruzphp6_lesson,
                                programmeruzphp7_lesson, programmeruzphp8_lesson, programmeruzphp9_lesson,
                                programmeruzphp10_lesson, programmeruzphp11_lesson, programmeruzphp12_lesson,
                                programmeruzphp13_lesson, programmeruzphp14_lesson, programmeruzphp15_lesson,
                                programmeruzphp16_lesson, programmeruzphp17_lesson, programmeruzphp18_lesson,
                                programmeruzphp19_lesson, programmeruzphp20_lesson, programmeruzphp21_lesson,
                                programmeruzphp22_lesson, programmeruzphp23_lesson,
                                programmeruzphp24_lesson, programmeruzphp25_lesson, programmeruzphp26_lesson,
                                programmeruzphp27_lesson, programmeruzphp28_lesson, programmeruzphp29_lesson,
                                programmeruzphp30_lesson, programmeruzphp31_lesson, programmeruzphp32_lesson,
                                programmeruzphp33_lesson, programmeruzphp34_lesson, programmeruzphp35_lesson)

        download_animation(message)
        msg = bot.send_message(message.chat.id, "Darslar bo'limi 📚"
                               , reply_markup=it_php_programmeruz)
        bot.register_next_step_handler(msg, darslar_python)

        #telegram bot yasash
    elif message.text == "Telegram Bot Yaratish (Python)":
        telegram_menulessons = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        telegram_menulessons.add(item1,botir_ziyotov)
        bot.send_message(message.chat.id, "Telegram bot yasash \n bo'yicha video darslar"
                         , reply_markup=telegram_menulessons)

    elif message.text == 'Botir Niyozov(Telegrambot yasash)':
        telegrambot_menu = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        telegrambot_menu.add(item1,botir_ziyotov_bot,botir_ziyotov_bot1,botir_ziyotov_bot2,botir_ziyotov_bot3)
        download_animation(message)
        msg = bot.send_message(message.chat.id, "Darslar bo'limi 📚"
                               , reply_markup=telegrambot_menu)
        bot.register_next_step_handler(msg, darslar_python)
        #code editors
    elif message.text == "📝 Kod Muharrirlari(Dasturlar)":
        it_editorlar_menyusi = types.ReplyKeyboardMarkup(row_width=2)
        it_editorlar_menyusi.add(item1,vscode_editor32, vscode_editor64, sublime32_editor,sublime64_editor,
                                 anaconda32_editor, anaconda64_editor)
        msg = bot.send_message(message.chat.id, "Kod editorlar (Dasturlar)", reply_markup=it_editorlar_menyusi)
        bot.register_next_step_handler(msg, darslar_python)

    elif message.text == '3D Grafika & PS 🏞':
        graphics_and_ps_menu = types.ReplyKeyboardMarkup(row_width=1)
        graphics_and_ps_menu.add(item1, speed_art)
        download_animation(message)
        bot.send_message(message.chat.id, "3D Grafika & Adobe Photoshop Menyusi 🖥", reply_markup=graphics_and_ps_menu)

    # speed art

    elif message.text == '3D Speed Art 🖥':
        speed_art_menu = types.ReplyKeyboardMarkup(row_width=1)
        speed_art_menu.add(item1, nextgengraphics_speedart)
        download_animation(message)
        bot.send_message(message.chat.id, "Speed Art videolar 📗 \nUlarning aftorlari 👨🏻‍🏫", reply_markup=speed_art_menu)

    elif message.text == "NextGen (YT: NextGenGraphicX) \n(C4D)":
        next_gen_speedart = types.ReplyKeyboardMarkup(row_width=1)
        next_gen_speedart.add(item1, asal_speed_art)
        download_animation(message)
        msg = bot.send_message(message.chat.id, "NGGX SpeedArt 🖥", reply_markup=next_gen_speedart)
        bot.register_next_step_handler(msg, darslar_python)


    else:
        download_animation(message)
        bot.send_message(message.chat.id, "✅<b>Bajarildi</b>", parse_mode='html')
        darslar_python(message)



def darslar_python(message):
    file_name = str(message.text)

    try:
        file_id = dars(file_name)
        try:
            bot.send_document(message.chat.id, f"{file_id}", caption=f"{file_name}"
                                                                     f"\n__________________________________________"
                                                                     f"\nDO'STLARINGIZ BILAN ULASHISH"
                                                                     f"\nLINK: @on_line_darslarbot"
                                                                     f"\n__________________________________________")
        except:
            bot.send_video(message.chat.id, f"{file_id}", caption=f"{file_name}"
                                                                  f"\n__________________________________________"
                                                                  f"\nDO'STLARINGIZ BILAN ULASHISH"
                                                                  f"\nLINK: @on_line_darslarbot"
                                                                  f"\n__________________________________________")

    except:
        """ if user tries to get non existing data this func will work! """

        bot.send_message(message.chat.id, f"Siz qidirgaan: <b><u><i>{message.text}</i></u></b> "
                                          f"\nbo'yicha hej narsa topilmadi😕"
                                          f"\n________________________________________"
                                          "\n‼️<i>Hozirda bizda IT dasturlash tillaridan</i>"
                         "\n<i>faqat</i> <b>Python  🐍, HTML</b> va <b>PHP</b> \n<i>darslari mavjud</i>"
                                          "\n_________________________________________"
                         "\n ♻️Tez kinlarda yangi darslarniham qo'shishga harakat qilamiz🤓"
                                          "\n_________________________________________"
                         "\nDO'STALRINGIZ BILAN ULASHING "
                         "\n<b>LINK</b>: <i>@on_line_darslarbot</i>", parse_mode="html")


bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
bot.polling(none_stop=True)