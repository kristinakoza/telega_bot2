<<<<<<< HEAD
import asyncio
import random

VOCABULARY = [
    {"word": "persistent", "meaning": "упорный", "example": "She is a persistent learner."},
    {"word": "curious", "meaning": "любознательный", "example": "He is always curious about how things work."},
    {"word": "efficient", "meaning": "эффективный", "example": "She is an efficient worker."},
    {"word": "diligent", "meaning": "старательный", "example": "The diligent student always completes his homework on time."},
    {"word": "ambitious", "meaning": "амбициозный", "example": "She has ambitious plans for her career."},
    {"word": "reliable", "meaning": "надежный", "example": "He is a reliable friend who always keeps his promises."},
    {"word": "versatile", "meaning": "универсальный", "example": "She is a versatile musician who plays multiple instruments."},
    {"word": "adaptable", "meaning": "адаптивный", "example": "Being adaptable helps him succeed in new environments."},
    {"word": "resilient", "meaning": "стойкий", "example": "Despite setbacks, she remained resilient and kept moving forward."},
    {"word": "meticulous", "meaning": "педантичный", "example": "His meticulous attention to detail ensures high-quality work."},
    {"word": "innovative", "meaning": "инновационный", "example": "The company is known for its innovative approach to technology."},
    {"word": "tenacious", "meaning": "цепкий", "example": "Her tenacious attitude helped her overcome many challenges."},
    {"word": "proactive", "meaning": "инициативный", "example": "A proactive employee takes action before problems arise."},
    {"word": "resourceful", "meaning": "изобретательный", "example": "He is resourceful and always finds creative solutions."},
    {"word": "conscientious", "meaning": "добросовестный", "example": "She is a conscientious worker who never cuts corners."},
]
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = '7269437234:AAEMtf5S6SQu1JXpITlYhGgrFzJBBInQT_I'

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("༄˖°.☕️.ೃ࿔📚*:･ Марафоны", callback_data='join')],
        [InlineKeyboardButton("𐙚‧₊˚📒✩ ₊˚☁️⊹♡ Бесплатная тренировка словарного запаса", callback_data='task')],
        [InlineKeyboardButton("ℹ️ Вопросы и ответы", callback_data='faq')],
        [InlineKeyboardButton("₊˚.🎧 ✩｡☕ 🤎 Уроки по английскому", callback_data='lessons')],
        [InlineKeyboardButton("˙✧˖°🎓 ༘⋆｡ ° Курсы по английскому", callback_data='courses')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("ˎˊ˗⋆｡°✩📄Привет! Что тебя интересует?", reply_markup=reply_markup)

async def back(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("❓ Есть ли место для занятий?", callback_data='faq_place')],
        [InlineKeyboardButton(" 💵Сколько стоит занятие?", callback_data='faq_price')],
        [InlineKeyboardButton(" 📚Есть ли пробное занятие?", callback_data='faq_prob')],
        [InlineKeyboardButton("❓Что за курс по английскому?", callback_data='faq_course')],
        [InlineKeyboardButton("📚Хочу посмотреть отзывы", callback_data='faq_reviews')],
        [InlineKeyboardButton("📝📚🙆🏻‍♀️О Кристине", callback_data='faq_kristina')],
        [InlineKeyboardButton("⬅️ Назад", callback_data='back_to_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("📌 Часто задаваемые вопросы:", reply_markup=reply_markup)

# Callback handler
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE): 
    query = update.callback_query
    await query.answer()

    if query.data == 'join':
        await query.edit_message_text("🎓 Следующий марафон состоится 13 июля!\nЦена: 1000 рублей с проверкой и обратной связью\n400 рублей без проверки\nНапишите @goat_eto_koza чтобы вступить или задать вопросы. Для возвращения назад, нажмите /back")

    elif query.data == 'task':
        vocab = random.choice(VOCABULARY)
        text = f"🧠 Слово дня: *{vocab['word']}* (adj.)\nЗначение: {vocab['meaning']}\nПример: {vocab['example']}\nДля возвращения назад нажмите /back"
        
        keyboard = [
            [InlineKeyboardButton("🔁 Другое слово", callback_data='task')],
            [InlineKeyboardButton("⬅️ Назад в меню", callback_data='back_to_menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

    elif query.data == 'lessons':
        await query.edit_message_text("🎓Уроки по английскому проходят в индивидуальном формате через Zoom. Больше информации: @goat_eto_koza.\nДля возвращения назад, нажмите /back")

    elif query.data == 'faq':
        keyboard = [
            [InlineKeyboardButton("❓ Есть ли место для занятий?", callback_data='faq_place')],
            [InlineKeyboardButton("💵 Сколько стоит занятие?", callback_data='faq_price')],
            [InlineKeyboardButton("📚 Есть ли пробное занятие?", callback_data='faq_prob')],
            [InlineKeyboardButton("❓ Что за курс по английскому?", callback_data='faq_course')],
            [InlineKeyboardButton("📚 Хочу посмотреть отзывы", callback_data='faq_reviews')],
            [InlineKeyboardButton("📝📚🙆🏻‍♀️ О Кристине", callback_data='faq_kristina')],
            [InlineKeyboardButton("⬅️ Назад", callback_data='back_to_menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📌 Часто задаваемые вопросы:", reply_markup=reply_markup)

    elif query.data == 'faq_place':
        back_button = InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Назад", callback_data='faq')]])
        await query.edit_message_text("📝 На июнь 2025 мест на данный момент нет. Напишите @goat_eto_koza чтобы занять очередь!\nДля возвращения назад, нажмите /back", reply_markup=back_button)


    elif query.data == 'faq_place':
        back_button = InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Назад", callback_data='faq')]])
        await query.edit_message_text("📝 На июнь 2025 мест на данный момент нет. Напишите @goat_eto_koza чтобы занять очередь!\nДля возвращения в меню, нажмите /back")
        

    elif query.data == 'faq_price':
        back_button = InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Назад", callback_data='faq')]])
        await query.edit_message_text("🌟 Занятия стоят 1300 рублей/час.\nДля возвращения в меню, нажмите /back")

    elif query.data == 'faq_prob':
        back_button = InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Назад", callback_data='faq')]])
        await query.edit_message_text("💰 Пробные занятия не предоставляются.\nДля возвращения в меню, нажмите /back")

    elif query.data == 'faq_course':
        back_button = InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Назад", callback_data='faq')]])
        await query.edit_message_text("🌟 Курс по бизнес-английскому для работы и жизни за рубежом стартует в августе-сентябре 2025. Цена — 5000₽, длительность — 30 дней. Подпишитесь на канал для новостей: https://t.me/kozagoat.\nДля возвращения в меню, нажмите /back")

    elif query.data == 'faq_reviews':
        back_button = InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Назад", callback_data='faq')]])
        await query.edit_message_text("🌟 Отзывы: https://docs.google.com/document/d/1ROCOQZK9hcrrPSy-VKbBQR_VbUQq3mfq8hv4REBzbQA/edit?tab=t.0\nКомментарии ВК: https://vk.com/market/product/individualnye-zanyatia-po-angliyskomu-yazyku-188039802-4150462.\nДля возвращения в меню, нажмите /back")

    elif query.data == 'faq_kristina':
        back_button = InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Назад", callback_data='faq')]])
        await query.edit_message_text("Кристина — создательница этого бота и каналов. Преподаю английский с 2018, сертифицирована TESOL, готовлю к IELTS и SAT. Подробнее: @goat_eto_koza.\nДля возвращения в меню, нажмите /back ")

    elif query.data == 'back_to_menu':
        back_button = InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Назад", callback_data='faq')]])
        await start(update, context)  # Return to start menu
        

# Run the bot
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))
app.add_handler(CommandHandler("back", back))

app.run_polling()
