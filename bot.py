import os
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# 从云端安全读取你的机器人 Token
TOKEN = os.environ.get("BOT_TOKEN")

# 当用户点击 /start 时触发
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 定义你要的按钮布局（仿照你截图中的菜单）
    keyboard = [
        [KeyboardButton("人工服务"), KeyboardButton("供应发布"), KeyboardButton("需求发布")],
        [KeyboardButton("TRX兑换"), KeyboardButton("中文翻译"), KeyboardButton("供应资源")],
        [KeyboardButton("加入会员"), KeyboardButton("我要担保"), KeyboardButton("申请公群")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(
        "欢迎来到服务中心！请点击下方菜单选择您需要的功能：",
        reply_markup=reply_markup
    )

# 当用户点击或者发送文字时触发的自动回复
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "人工服务":
        await update.message.reply_text("已为您转接人工客服，请留言您的问题，超过30分钟无人回复将由值班人员跟进。")
    elif text == "TRX兑换":
        await update.message.reply_text("当前 TRX 实时兑换通道：请直接联系管理员进行兑换。")
    else:
        await update.message.reply_text(f"您点击了：{text}，系统正在处理中...")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    
    print("机器人已成功启动...")
    app.run_polling()