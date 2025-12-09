import telebot
from telebot import types
import os

BOT_TOKEN = os.environ.get('8463880587:AAHll1-aQT9ElORnmSc1VAJDud-plaskTbs')
bot = telebot.TeleBot(8463880587:AAHll1-aQT9ElORnmSc1VAJDud-plaskTbs)

CHANNEL_USERNAME = "@tgpremiumsubscription"
CHANNEL_ID = "@tgpremiumsubscription"

LINKS = {
    '5': {'bsb': 'https://sor-soch.com/bsb.php?klass=5', 'chsb': 'https://sor-soch.com/chsb.php?klass=5'},
    '6': {'bsb': 'https://sor-soch.com/bsb.php?klass=6', 'chsb': 'https://sor-soch.com/chsb.php?klass=6'},
    '7': {'bsb': 'https://sor-soch.com/bsb.php?klass=7', 'chsb': 'https://sor-soch.com/chsb.php?klass=7'},
    '8': {'bsb': 'https://sor-soch.com/bsb.php?klass=8', 'chsb': 'https://sor-soch.com/chsb.php?klass=8'},
    '9': {'bsb': 'https://sor-soch.com/bsb.php?klass=9', 'chsb': 'https://sor-soch.com/chsb.php?klass=9'},
    '10': {'bsb': 'https://sor-soch.com/bsb.php?klass=10', 'chsb': 'https://sor-soch.com/chsb.php?klass=10'},
    '11': {'bsb': 'https://sor-soch.com/bsb.php?klass=11', 'chsb': 'https://sor-soch.com/chsb.php?klass=11'}
}

def check_subscription(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except:
        return False

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if not check_subscription(user_id):
        markup = types.InlineKeyboardMarkup()
        btn_channel = types.InlineKeyboardButton("📢 Kanalga obuna bo'lish", url=f"https://t.me/{CHANNEL_USERNAME[1:]}")
        btn_check = types.InlineKeyboardButton("✅ Obunani tekshirish", callback_data="check_subscription")
        markup.add(btn_channel)
        markup.add(btn_check)
        bot.send_message(message.chat.id, "👋 Assalomu alaykum!\n\nBotdan foydalanish uchun avval kanalimizga obuna bo'ling:\n\n📢 " + CHANNEL_USERNAME, reply_markup=markup)
        return
    show_main_menu(message.chat.id)

def show_main_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btns = [types.KeyboardButton(f"📚 {i}-sinf") for i in range(5, 12)]
    markup.add(*btns)
    bot.send_message(chat_id, "📖 *BSB va CHSB javoblar botiga xush kelibsiz!*\n\nO'zingizga kerakli sinfni tanlang:", parse_mode="Markdown", reply_markup=markup)

@bot.message_handler(func=lambda m: any(f"{i}-sinf" in m.text for i in range(5, 12)))
def select_class(message):
    user_id = message.from_user.id
    if not check_subscription(user_id):
        markup = types.InlineKeyboardMarkup()
        btn_channel = types.InlineKeyboardButton("📢 Kanalga obuna bo'lish", url=f"https://t.me/{CHANNEL_USERNAME[1:]}")
        btn_check = types.InlineKeyboardButton("✅ Obunani tekshirish", callback_data="check_subscription")
        markup.add(btn_channel)
        markup.add(btn_check)
        bot.send_message(message.chat.id, "❌ Botdan foydalanish uchun kanalimizga obuna bo'ling!", reply_markup=markup)
        return
    
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
        bot.send_message(message.chat.id, f"📚 *{class_num}-sinf tanlandi*\n\nKerakli bo'limni tanlang:", parse_mode="Markdown", reply_markup=markup)
        bot.register_next_step_handler(message, lambda m: handle_selection(m, class_num))

def handle_selection(message, class_num):
    user_id = message.from_user.id
    if not check_subscription(user_id):
        markup = types.InlineKeyboardMarkup()
        btn_channel = types.InlineKeyboardButton("📢 Kanalga obuna bo'lish", url=f"https://t.me/{CHANNEL_USERNAME[1:]}")
        btn_check = types.InlineKeyboardButton("✅ Obunani tekshirish", callback_data="check_subscription")
        markup.add(btn_channel)
        markup.add(btn_check)
        bot.send_message(message.chat.id, "❌ Botdan foydalanish uchun kanalimizga obuna bo'ling!", reply_markup=markup)
        return
    
    if "⬅️ Orqaga" in message.text:
        show_main_menu(message.chat.id)
        return
    
    if "BSB javoblar" in message.text:
        link = LINKS[class_num]['bsb']
        markup = types.InlineKeyboardMarkup()
        btn_open = types.InlineKeyboardButton("🔓 Ochish", url=link)
        markup.add(btn_open)
        bot.send_message(message.chat.id, f"📝 *{class_num}-sinf BSB javoblar*\n\nJavoblarni ko'rish uchun quyidagi tugmani bosing:", parse_mode="Markdown", reply_markup=markup)
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn_bsb = types.KeyboardButton("📝 BSB javoblar")
        btn_chsb = types.KeyboardButton("📋 CHSB javoblar")
        btn_back = types.KeyboardButton("⬅️ Orqaga")
        markup2.add(btn_bsb, btn_chsb)
        markup2.add(btn_back)
        bot.send_message(message.chat.id, "Yana tanlashingiz mumkin:", reply_markup=markup2)
        bot.register_next_step_handler(message, lambda m: handle_selection(m, class_num))
        
    elif "CHSB javoblar" in message.text:
        link = LINKS[class_num]['chsb']
        markup = types.InlineKeyboardMarkup()
        btn_open = types.InlineKeyboardButton("🔓 Ochish", url=link)
        markup.add(btn_open)
        bot.send_message(message.chat.id, f"📋 *{class_num}-sinf CHSB javoblar*\n\nJavoblarni ko'rish uchun quyidagi tugmani bosing:", parse_mode="Markdown", reply_markup=markup)
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn_bsb = types.KeyboardButton("📝 BSB javoblar")
        btn_chsb = types.KeyboardButton("📋 CHSB javoblar")
        btn_back = types.KeyboardButton("⬅️ Orqaga")
        markup2.add(btn_bsb, btn_chsb)
        markup2.add(btn_back)
        bot.send_message(message.chat.id, "Yana tanlashingiz mumkin:", reply_markup=markup2)
        bot.register_next_step_handler(message, lambda m: handle_selection(m, class_num))
    else:
        bot.register_next_step_handler(message, lambda m: handle_selection(m, class_num))

@bot.callback_query_handler(func=lambda call: call.data == "check_subscription")
def check_sub_callback(call):
    user_id = call.from_user.id
    if check_subscription(user_id):
        bot.answer_callback_query(call.id, "✅ Obuna tasdiqlandi!")
        bot.delete_message(call.message.chat.id, call.message.message_id)
        show_main_menu(call.message.chat.id)
    else:
        bot.answer_callback_query(call.id, "❌ Siz hali kanalga obuna bo'lmadingiz!", show_alert=True)

if __name__ == "__main__":
    print("🤖 Bot ishga tushdi...")
    bot.infinity_polling()
