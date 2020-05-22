import COVID19Py
import telebot
from telebot import types


covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('1220076202:AAFIt-ri8Zwg69G4HrLEO4WGgPYPXd833A0')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('По всьому світу')
    btn2 = types.KeyboardButton('Україна')
    btn3 = types.KeyboardButton('Росія');
    btn4 = types.KeyboardButton('Білорусь')
    markup.add(btn1, btn2, btn3, btn4)

    send_message = f"<b>Привет {message.from_user.first_name}!</b>\nЧтобы узнать данные про коронавируса напишите " \
		f"название страны, например: США, Україна, Росія и так дальше\n"
    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def mess(message):
    final_message=""
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "сша":
        location = covid19.getLocationByCountryCode("US")
    elif get_message_bot == "україна":
        location = covid19.getLocationByCountryCode("UA")
    elif get_message_bot == "росія":
        location = covid19.getLocationByCountryCode("RU")
    elif get_message_bot == "білорусь":
        location = covid19.getLocationByCountryCode("BY")
    elif get_message_bot == "італія":
        location = covid19.getLocationByCountryCode("IT")
    else:
        location = covid19.getLatest()
        final_message = f"<u>Дані по всьому світу:</u>\n<b> Захворіли: </b> {location['confirmed']:,}\n<b>Смертей: </b>{location['deaths']:,}"

    if final_message == "":
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<u>Дані по країні:</u>\nНаселення: {location[0]['country_population']:,}\n" \
                        f"Останнє оновлення: {date[0]} {time[0]}\nОстанні дані:\n<b>" \
                        f"Захворілих: </b>{location[0]['latest']['confirmed']:,}\n<b>Сметрей: </b>" \
                        f"{location[0]['latest']['deaths']:,}"

    bot.send_message(message.chat.id, final_message, parse_mode='html')

bot.polling(none_stop=True)
latest = covid19.getLatest()
print (latest)