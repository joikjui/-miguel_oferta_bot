import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8740673934:AAEQ8lKmVoxlS2b32WS3lq4uSr56FFjgk6o"

logging.basicConfig(level=logging.INFO)

# Links seus afiliados
LINKS = {
    'shopee': 'https://shopee.com.br/search?sub_id=geog2',
    'ali': 'https://pt.aliexpress.com?aff_platform=portals.aliexpress.com',
    'ml': 'https://afiliados.mercadolivre.com.br/ofertas',
    'amazon': 'https://amazon.com.br?tag=geog2-20'
}

def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [['/ofertas', '/cupom'], ['/shopee', '/ali'], ['/ml', '/amazon']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "🚀 *GeoOffset G2 ATIVO!*\n\n"
        "Toque nos botões ou comandos 👇",
        reply_markup=reply_markup, parse_mode='Markdown'
    )

async def ofertas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = "🔥 *OFERTAS 4 LOJAS*:\n\n"
    for loja, link in LINKS.items():
        msg += f"🛒 {loja.upper()}: {link}\n"
    await update.message.reply_text(msg, parse_mode='Markdown')

async def cupom(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💰 *CUPONS ATIVOS 2026*:\n"
        "Shopee: OFF10G2\n"
        "Ali: GEO10\n"
        "ML: MLG215OFF\n"
        "Amazon: PRIME20"
    )

async def shopee(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🛒 *SHOPEE OFERTAS*\n{LINKS['shopee']}\nCupom: OFF10G2")

async def ali(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🌍 *ALIEXPRESS*\n{LINKS['ali']}\nCupom: GEO10")

async def ml(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🏪 *MERCADO LIVRE*\n{LINKS['ml']}\nCupom: MLG215OFF")

async def amazon(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"📦 *AMAZON*\n{LINKS['amazon']}\nCupom: PRIME20")

async def qualquer_texto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()
    if 'shopee' in texto:
        await shopee(update, context)
    elif 'ali' in texto:
        await ali(update, context)
    elif 'cupom' in texto:
        await cupom(update, context)
    else:
        await update.message.reply_text("Use /start")

def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ofertas", ofertas))
    app.add_handler(CommandHandler("cupom", cupom))
    app.add_handler(CommandHandler("shopee", shopee))
    app.add_handler(CommandHandler("ali", ali))
    app.add_handler(CommandHandler("ml", ml))
    app.add_handler(CommandHandler("amazon", amazon))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, qualquer_texto))
    
    print("✅ GeoOffset G2 rodando!")
    app.run_polling()

if __name__ == '__main__':
    main()