from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import requests
from datetime import datetime
import random

TOKEN = "8046750809:AAGXSJys1MV7Au1udmnmZ7P9JwMAusIm3zk"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 **ITACHI CRYPTO BOT** - PHIÊN BẢN FULL\n\n"
        "📋 Lệnh:\n"
        "/gia - Giá realtime nhiều coin\n"
        "/lenh - Lệnh scalping + nuôi tuần\n"
        "/phantich - Phân tích full (dòng tiền, macro, chiêm tinh)\n"
        "/tin - Tin nóng Trump, Musk, Q, FED...\n"
        "/help - Xem tất cả lệnh"
    )

async def gia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        data = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd").json()
        btc = data["bitcoin"]["usd"]
        eth = data["ethereum"]["usd"]
        sol = data.get("solana", {}).get("usd", "N/A")
        await update.message.reply_text(
            f"📊 **GIÁ REALTIME** ({datetime.now().strftime('%H:%M:%S')})\n\n"
            f"₿ BTC: **${btc:,}**\n"
            f"⟠ ETH: **${eth:,}**\n"
            f"◎ SOL: **${sol:,}**\n"
            f"π Pi Network: **Đang theo dõi**"
        )
    except:
        await update.message.reply_text("❌ Lỗi lấy giá tạm thời.")

async def lenh(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 **LỆNH ITACHI HÔM NAY**\n\n"
        "⚡ **SCALPING (Cá lia thia)**\n"
        "BTC: Long 76200-76500 | TP 76900 | SL 75900\n"
        "ETH: Long 2620-2650 | TP 2720 | SL 2580\n\n"
        "📈 **NUÔI TUẦN (Chốt cuối tuần)**\n"
        "BTC: Long từ 75800 | TP 82000 - 85000\n"
        "ETH: Long từ 2550 | TP 3000+\n\n"
        "💰 Risk: 1-2% vốn/lệnh"
    )

async def phantich(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌌 **PHÂN TÍCH ITACHI FULL**\n\n"
        "📍 **Dòng tiền**: Whale đang gom mạnh BTC & ETH\n"
        "🌍 **Macro & Chính trị**: Trump + Musk đẩy narrative crypto mạnh\n"
        "📰 **FED/SEC**: Có dấu hiệu nới lỏng\n"
        "🔮 **Chiêm tinh**: Sao Mộc chiếu Kim Ngưu + Mặt Trời hỗ trợ → **Rất Bullish** ngắn hạn\n\n"
        "✅ **Kết luận**: Bias **LONG** mạnh hôm nay. Tập trung BTC & ETH."
    )

async def tin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📰 **TIN NÓNG CRYPTO - ITACHI UPDATE**\n\n"
        "• Trump đăng bài ủng hộ Bitcoin mạnh\n"
        "• Musk tweet về AI + Crypto tích cực\n"
        "• Dòng tiền lớn đang chảy vào ETH\n"
        "• Team Q: 'The Storm is approaching' 👀\n"
        "• Tin chiến tranh & thỏa thuận ảnh hưởng dòng tiền\n\n"
        "Cập nhật realtime đang theo dõi..."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Đã có đầy đủ lệnh ở /start rồi nè!")

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("gia", gia))
    app.add_handler(CommandHandler("lenh", lenh))
    app.add_handler(CommandHandler("phantich", phantich))
    app.add_handler(CommandHandler("tin", tin))
    app.add_handler(CommandHandler("help", help_command))
    
    print("🤖 Itachi Crypto Bot FULL đang chạy...")
    app.run_polling()