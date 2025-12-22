import telebot
from telebot import types

# Bot tokeni
BOT_TOKEN = "8463880587:AAHll1-aQT9ElORnmSc1VAJDud-plaskTbs"
bot = telebot.TeleBot(BOT_TOKEN)

# Majburiy kanal
CHANNEL_USERNAME = "@tgpremiumsubscription"
CHANNEL_ID = "@tgpremiumsubscription"

# BSB va CHSB havolalari
LINKS = {
    '5': {
        'bsb': 'https://sor-soch.com/bsb.php?klass=5',
        'chsb': 'https://sor-soch.com/chsb.php?klass=5'
    },
    '6': {
        'bsb': 'https://sor-soch.com/bsb.php?klass=6',
        'chsb': 'https://sor-soch.com/chsb.php?klass=6'
    },
    '7': {
        'bsb': 'https://sor-soch.com/bsb.php?klass=7',
        'chsb': 'https://sor-soch.com/chsb.php?klass=7'
    },
    '8': {
        'bsb': 'https://sor-soch.com/bsb.php?klass=8',
        'chsb': 'https://sor-soch.com/chsb.php?klass=8'
    },
    '9': {
        'bsb': 'https://sor-soch.com/bsb.php?klass=9',
        'chsb': 'https://sor-soch.com/chsb.php?klass=9'
    },
    '10': {
        'bsb': 'https://sor-soch.com/bsb.php?klass=10',
        'chsb': 'https://sor-soch.com/chsb.php?klass=10'
    },
    '11': {
        'bsb': 'https://sor-soch.com/bsb.php?klass=11',
        'chsb': 'https://sor-soch.com/chsb.php?klass=11'
    }
}


# Kanalga obuna bo'lganligini tekshirish
def check_subscription(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except:
        return False


# Start komandasi
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id

    # Obuna tekshiruvi
    if not check_subscription(user_id):
        markup = types.InlineKeyboardMarkup()
        btn_channel = types.InlineKeyboardButton("📢 Kanalga obuna bo'lish", url=f"https://t.me/{CHANNEL_USERNAME[1:]}")
        btn_check = types.InlineKeyboardButton("✅ Obunani tekshirish", callback_data="check_subscription")
        markup.add(btn_channel)
        markup.add(btn_check)

        bot.send_message(
            message.chat.id,
            "👋 Assalomu alaykum!\n\n"
            "Botdan foydalanish uchun avval kanalimizga obuna bo'ling:\n\n"
            f"📢 {CHANNEL_USERNAME}",
            reply_markup=markup
        )
        return

    # Asosiy menyu
    show_main_menu(message.chat.id)


# Asosiy menyuni ko'rsatish
def show_main_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("📚 5-sinf")
    btn2 = types.KeyboardButton("📚 6-sinf")
    btn3 = types.KeyboardButton("📚 7-sinf")
    btn4 = types.KeyboardButton("📚 8-sinf")
    btn5 = types.KeyboardButton("📚 9-sinf")
    btn6 = types.KeyboardButton("📚 10-sinf")
    btn7 = types.KeyboardButton("📚 11-sinf")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)

    bot.send_message(
        chat_id,
        "📖 *BSB va CHSB javoblar botiga xush kelibsiz!*\n\n"
        "O'zingizga kerakli sinfni tanlang:",
        parse_mode="Markdown",
        reply_markup=markup
    )


# Sinf tanlanganda
@bot.message_handler(func=lambda message: any(f"{i}-sinf" in message.text for i in range(5, 12)))
def select_class(message):
    user_id = message.from_user.id

    # Obuna tekshiruvi
    if not check_subscription(user_id):
        markup = types.InlineKeyboardMarkup()
        btn_channel = types.InlineKeyboardButton("📢 Kanalga obuna bo'lish", url=f"https://t.me/{CHANNEL_USERNAME[1:]}")
        btn_check = types.InlineKeyboardButton("✅ Obunani tekshirish", callback_data="check_subscription")
        markup.add(btn_channel)
        markup.add(btn_check)

        bot.send_message(
            message.chat.id,
            "❌ Botdan foydalanish uchun kanalimizga obuna bo'ling!",
            reply_markup=markup
        )
        return

    # Sinfni aniqlash
    class_num = None
    for i in range(5, 12):
        if f"{i}-sinf" in message.text:
            class_num = str(i)
            break

    if class_num:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn_bsb = types.KeyboardButton("📝 BSB javoblar")
        btn_chsb = types.KeyboardButton("📋 CHSB javoblar")
        btn_back = types.KeyboardButton("⬅️ Orqaga")
        markup.add(btn_bsb, btn_chsb)
        markup.add(btn_back)

        bot.send_message(
            message.chat.id,
            f"📚 *{class_num}-sinf tanlandi*\n\n"
            "Kerakli bo'limni tanlang:",
            parse_mode="Markdown",
            reply_markup=markup
        )

        # Keyingi qadamni kutish
        bot.register_next_step_handler(message, lambda m: handle_selection(m, class_num))


# BSB/CHSB tanlash
def handle_selection(message, class_num):
    user_id = message.from_user.id

    # Obuna tekshiruvi
    if not check_subscription(user_id):
        markup = types.InlineKeyboardMarkup()
        btn_channel = types.InlineKeyboardButton("📢 Kanalga obuna bo'lish", url=f"https://t.me/{CHANNEL_USERNAME[1:]}")
        btn_check = types.InlineKeyboardButton("✅ Obunani tekshirish", callback_data="check_subscription")
        markup.add(btn_channel)
        markup.add(btn_check)

        bot.send_message(
            message.chat.id,
            "❌ Botdan foydalanish uchun kanalimizga obuna bo'ling!",
            reply_markup=markup
        )
        return

    if "⬅️ Orqaga" in message.text:
        show_main_menu(message.chat.id)
        return

    if "BSB javoblar" in message.text:
        link = LINKS[class_num]['bsb']
        markup = types.InlineKeyboardMarkup()
        btn_open = types.InlineKeyboardButton("🔓 Ochish", url=link)
        markup.add(btn_open)

        bot.send_message(
            message.chat.id,
            f"📝 *{class_num}-sinf BSB javoblar*\n\n"
            "Javoblarni ko'rish uchun quyidagi tugmani bosing:",
            parse_mode="Markdown",
            reply_markup=markup
        )

        # Yana tanlash imkoniyati
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn_bsb = types.KeyboardButton("📝 BSB javoblar")
        btn_chsb = types.KeyboardButton("📋 CHSB javoblar")
        btn_back = types.KeyboardButton("⬅️ Orqaga")
        markup2.add(btn_bsb, btn_chsb)
        markup2.add(btn_back)

        bot.send_message(
            message.chat.id,
            "Yana tanlashingiz mumkin:",
            reply_markup=markup2
        )
        bot.register_next_step_handler(message, lambda m: handle_selection(m, class_num))

    elif "CHSB javoblar" in message.text:
        link = LINKS[class_num]['chsb']
        markup = types.InlineKeyboardMarkup()
        btn_open = types.InlineKeyboardButton("🔓 Ochish", url=link)
        markup.add(btn_open)

        bot.send_message(
            message.chat.id,
            f"📋 *{class_num}-sinf CHSB javoblar*\n\n"
            "Javoblarni ko'rish uchun quyidagi tugmani bosing:",
            parse_mode="Markdown",
            reply_markup=markup
        )

        # Yana tanlash imkoniyati
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn_bsb = types.KeyboardButton("📝 BSB javoblar")
        btn_chsb = types.KeyboardButton("📋 CHSB javoblar")
        btn_back = types.KeyboardButton("⬅️ Orqaga")
        markup2.add(btn_bsb, btn_chsb)
        markup2.add(btn_back)

        bot.send_message(
            message.chat.id,
            "Yana tanlashingiz mumkin:",
            reply_markup=markup2
        )
        bot.register_next_step_handler(message, lambda m: handle_selection(m, class_num))
    else:
        bot.register_next_step_handler(message, lambda m: handle_selection(m, class_num))


# Callback query handler (obuna tekshirish uchun)
@bot.callback_query_handler(func=lambda call: call.data == "check_subscription")
def check_sub_callback(call):
    user_id = call.from_user.id

    if check_subscription(user_id):
        bot.answer_callback_query(call.id, "✅ Obuna tasdiqlandi!")
        bot.delete_message(call.message.chat.id, call.message.message_id)
        show_main_menu(call.message.chat.id)
    else:
        bot.answer_callback_query(call.id, "❌ Siz hali kanalga obuna bo'lmadingiz!", show_alert=True)


# Botni ishga tushirish
print("🤖 Bot ishga tushdi...")
bot.infinity_polling()
