import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext, CallbackQueryHandler, MessageHandler, filters

logging.basicConfig(filename='iranflightbot_log.txt', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

ADMIN_USER_ID = 1485409432 
user_states = {}

async def say_hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("User {} with username {} started the bot.".format(user.full_name, user.username))
    logging.getLogger("httpx").setLevel(logging.WARNING)

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(text="🤑درآمد مسافر", url="https://t.me/koolbar_bot"),
            InlineKeyboardButton(text="ℹ️دانستنی ها", callback_data="wikibutton"),
        ],
        [
            InlineKeyboardButton(text="💵پرداخت ارزی", url="https://t.me/vlansupport"),
            InlineKeyboardButton(text="🧳پست سریع هوایی", url="https://t.me/koolbar_bot"),
        ],
        [
            InlineKeyboardButton(text="💬گروه ها", callback_data="groupslist"),
            InlineKeyboardButton(text="🌦آب و هوا", url="https://www.accuweather.com/fa"),
        ],
        [
            InlineKeyboardButton(text="🛫اطلاعات پرواز فرودگاه", url="https://fids.airport.ir/"),
        ],
        [
            InlineKeyboardButton(text="✈️وضعیت لحظه ای هواپیما", url="https://www.flightradar24.com/32.61,54.76/6"),
        ],
        [
            InlineKeyboardButton(text="⏱بلیط لحظه آخری", callback_data="lastsecondbutt"),
            InlineKeyboardButton(text="🗂راهنمای ویزا", callback_data="visaguide"),
        ],
        [
            InlineKeyboardButton(text="📲ارتباط باما", callback_data="aboutus"),
            InlineKeyboardButton(text="✈️یافتن همسفر", callback_data="بزودی"),
        ],
    ])

    await update.message.reply_text("ربات فلایت ایران یک ربات جامع کاربردی است که خدمات مختلفی همچون ارسال هوایی بار ، کسب درآمد برای مسافر،انجام پرداخت های ارزی مانند پرداختی های سفارت ، معرفی بلیط های لحظه آخری و یک مرجع کامل از اطلاعات مورد نیاز هر مسافر است🤖. ", reply_markup=keyboard)

async def button_controller(update: Update, context: CallbackContext):
    data = update.callback_query.data
    user = update.callback_query.from_user
    logger.info("User {} (Username: {}) clicked on button: {}".format(user.first_name, user.username, data))

    if data == "aboutus":
        await update.callback_query.message.edit_text("بسیار خرسند می شویم که نظرات خود را با ما را در میان بگذارید.جهت تبلیغات و سایر موارد لطفا به ما پیام دهید😍 @vlansupport", reply_markup=None)
    elif data == "forbiddenflightrules":
        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(text="🇨🇦کانادا", url="https://t.me/koolbar_international/81"),
                InlineKeyboardButton(text="🇮🇹ایتالیا", url="https://t.me/koolbar_international/508"),
                InlineKeyboardButton(text="🇮🇷ایران", url="https://www.alibaba.ir/mag/travel-facts/customs-regulations-travelers-luggage/"),
            ],
            [
                InlineKeyboardButton(text="🇬🇧انگلیس", url="https://t.me/koolbar_international/540"),
                InlineKeyboardButton(text="🇺🇸آمریکا", url="https://t.me/koolbar_international/542"),
                InlineKeyboardButton(text="🇪🇺اروپا", url="https://t.me/koolbar_international/636"),
            ],
            [
                InlineKeyboardButton(text="🇮🇷ایران", url="https://t.me/koolbar_international/637"),
            ],
        ])

        await update.callback_query.message.edit_text("لطفا تاریخ بروزرسانی را دقت نمایید و حتما منبع خود را وبسایت رسمی آن کشور مد نظر قرار دهید ", reply_markup=keyboard)
    elif data == "lastsecondbutt":
        await update.callback_query.message.reply_text("جهت دریافت بهترین نرخ پرواز, لطفا مشابه پیام نمونه ارسال نمایید. مبدا ، مقصد و زمان پیشنهادی (تهران، تورنتو ، ۲۰ الی ۲۵ مرداد)")
        user_states[user.id] = "awaiting_admin_message"
    elif data == "websiteslist":
        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(text="🇨🇦کانادا", url="https://t.me/koolbar_international/560"),
                InlineKeyboardButton(text="🇮🇹ایتالیا", url="https://t.me/koolbar_international/562"),
                InlineKeyboardButton(text="🇮🇶عراق", url="https://t.me/koolbar_international/566"),
            ],
            [
                InlineKeyboardButton(text="🇬🇧انگلیس", url="https://t.me/koolbar_international/563"),
                InlineKeyboardButton(text="🇺🇸آمریکا", url="https://t.me/koolbar_international/564"),
                InlineKeyboardButton(text="🇪🇺اروپا", url="https://t.me/koolbar_international/565"),
            ],
        ])
        await update.callback_query.message.edit_text("لطفا تاریخ بروزرسانی را دقت نمایید و حتما منبع خود را وبسایت رسمی آن کشور مد نظر قرار دهید ", reply_markup=keyboard)
    elif data == "wikibutton":
        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(text="📄دریافت پاسپورت", url="https://t.me/koolbar_international/526"),
                InlineKeyboardButton(text="🧑‍🎓معافیت تحصیلی", url="https://t.me/koolbar_international/503"),
            ],
            [
                InlineKeyboardButton(text="❌ممنوع الخروجی", url="https://t.me/koolbar_international/527"),
                InlineKeyboardButton(text="🚫کالا های ممنوعه", url="https://t.me/koolbar_international/637"),
            ],
            [
                InlineKeyboardButton(text="💸عوارض خروج از کشور", url="https://t.me/koolbar_international/516"),
                InlineKeyboardButton(text="🛡بیمه مسافرتی", url="https://t.me/koolbar_international/549"),
            ],
            [
                InlineKeyboardButton(text="💶قیمت ارز", url="https://www.tgju.org/currency"),
                InlineKeyboardButton(text="⚠️ممنوعیت های هوایی", callback_data="forbiddenflightrules"),
            ],
        ])
        await update.callback_query.message.edit_text("هر آنچه که در خصوص خروج از کشور نیاز دارید که بدانید در این بخش آشنا می شوید", reply_markup=keyboard)
    elif data == "visaguide":
        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(text="اصطلاحات", callback_data="بزودی"),
            ],
            [
                InlineKeyboardButton(text="🇬🇧انگلیس", callback_data="بزودی"),
                InlineKeyboardButton(text="🇺🇸آمریکا", callback_data="بزودی"),
                InlineKeyboardButton(text="🇨🇦کانادا", callback_data="بزودی"),
                InlineKeyboardButton(text="🇮🇹ایتالیا", callback_data="بزودی"),
            ],
            [
                InlineKeyboardButton(text="❗️سایر کشور ها", callback_data="بزودی"),
            ],
        ])
        await update.callback_query.message.edit_text("⚠️⚠️ این بخش در حال بروز رسانی است و هیچ کدام یک از گزینه ها اطلاعاتی در اختیار شما قرار نمی دهد", reply_markup=keyboard)
    elif data == "groupslist":
        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(text="🇨🇦کانادا", url="https://t.me/koolbar_international/485"),
                InlineKeyboardButton(text="🇮🇹ایتالیا", url="https://t.me/koolbar_international/582"),
                InlineKeyboardButton(text="🇮🇶عراق", url="https://t.me/koolbar_international/583"),
            ],
            [
                InlineKeyboardButton(text="🇬🇧انگلیس", url="https://t.me/koolbar_international/584"),
                InlineKeyboardButton(text="🇺🇸آمریکا", url="https://t.me/koolbar_international/585"),
                InlineKeyboardButton(text="🇪🇺اروپا", url="https://t.me/koolbar_international/586"),
            ],
            [
                InlineKeyboardButton(text="🇪🇸اسپانیا", url="https://t.me/koolbar_international/650"),
                InlineKeyboardButton(text="🇫🇷فرانسه", url="https://t.me/koolbar_international/651"),
                InlineKeyboardButton(text="🇹🇷ترکیه", url="https://t.me/koolbar_international/652"),
            ],
            [
                InlineKeyboardButton(text="🇳🇱هلند", url="https://t.me/koolbar_international/653"),
                InlineKeyboardButton(text="🇩🇪آلمان", url="https://t.me/koolbar_international/654"),
                InlineKeyboardButton(text="🇦🇺استرالیا", url="https://t.me/koolbar_international/655"),
            ],
            [
                InlineKeyboardButton(text="❗️سایر موارد", callback_data="https://t.me/koolbar_international/587"),
                InlineKeyboardButton(text="💬زبان خارجه", url="https://t.me/koolbar_international/639"),
            ],
        ])
        await update.callback_query.message.edit_text("🟦در این بخش لیست کاملی از کانال و گروه های مختلف هر کشور به تفکیک برای شما عزیزان فراهم گردیده است. همچنین در صورتی که می خواهید اطلاعات خود را نیز اضافه نمایید لطفا در بخش ارتباط با ما پیام خود را ارسال نمایید♥️", reply_markup=keyboard)
    else:
        await update.callback_query.answer(text=data, show_alert=True)
        await update.callback_query.message.reply_text(data)

async def handle_user_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    if user_states.get(user.id) == "awaiting_admin_message":
        admin_message = f"Message from {user.full_name} (Username: @{user.username}):\n\n{update.message.text}"
        await context.bot.send_message(chat_id=ADMIN_USER_ID, text=admin_message)
        await update.message.reply_text("بزودی مطابق درخواست شما، پرواز های مناسب ارسال خواهد شد")
        user_states[user.id] = None
    else:
        await forward_message_to_user(update, context)

async def forward_message_to_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    if user.id == ADMIN_USER_ID:
        try:
            target_username, message_text = update.message.text.split(maxsplit=1)
            target_user_id = await get_user_id_by_username(context, target_username[1:])  # Remove "@" from username
            if target_user_id:
                await context.bot.send_message(chat_id=target_user_id, text=message_text)
                await update.message.reply_text(f"Message sent to {target_username}")
            else:
                await update.message.reply_text(f"User {target_username} not found")
        except ValueError:
            await update.message.reply_text("Invalid format. Use: @username message")

async def get_user_id_by_username(context: ContextTypes.DEFAULT_TYPE, username: str):
    for user_id, state in user_states.items():
        chat_member = await context.bot.get_chat_member(chat_id=user_id, user_id=user_id)
        if chat_member.user.username == username:
            return user_id
    return None

TOKEN = "7185515791:AAHSS8rjTpeZWkEOe3G3i9MqF2PpUvuAYS8"
application = ApplicationBuilder().token(TOKEN).build()
application.add_handler(CommandHandler("start", say_hello))
application.add_handler(CallbackQueryHandler(button_controller))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_user_message))
application.run_polling(allowed_updates=Update.ALL_TYPES)