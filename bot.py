#!/usr/bin/env python3
import logging
import os
from threading import Thread

import telebot
from telebot import types
import yt_dlp
from flask import Flask

# ==========================================
# 👇 AAPKI DETAILS (PRE-SET)
# ==========================================
API_TOKEN = '8552567148:AAFX7Pv2X0U3kVoZ-Ks4zxCytv-1r_DKPKQ'
ADMIN_ID = 5235560672
# ==========================================

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)


@app.route('/')
def home():
    return "🚀 BOT IS ONLINE!"


def run_server():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    Thread(target=run_server, daemon=True).start()


def download_video_thread(message, url):
    chat_id = message.chat.id
    filename = f"vid_{chat_id}.mp4"
    try:
        msg = bot.send_message(chat_id, "⏳ **Video dhoondh raha hu...**")
        ydl_opts = {'format': 'best', 'outtmpl': filename, 'quiet': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        bot.edit_message_text("✅ **Uploading...**", chat_id, msg.message_id)
        with open(filename, 'rb') as video:
            bot.send_video(chat_id, video, caption="Lo Boss! 🔥")
    except Exception:
        logging.exception("Download or upload failed")
        bot.send_message(chat_id, "❌ Error: Link galat hai.")
    finally:
        if os.path.exists(filename):
            try:
                os.remove(filename)
            except Exception:
                logging.exception("Failed to remove temporary file")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    name = message.from_user.first_name or "Friend"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🎮 BGMI", "🎵 Songs", "🛠️ Tools")
    bot.reply_to(
        message,
        f"👋 **Namaste {name}!**\nBot taiyar hai. Link bhejo video ke liye.",
        reply_markup=markup,
    )


@bot.message_handler(func=lambda message: True)
def handle_all(message):
    text = (message.text or "").lower()
    if "instagram.com" in text or "youtu" in text:
        Thread(target=download_video_thread, args=(message, message.text), daemon=True).start()
    elif "bgmi" in text:
        bot.reply_to(message, "🔫 **BGMI Sens:** `7052-8888-0000`")
    elif "songs" in text or "🎵" in message.text:
        bot.reply_to(message, "🎧 **Trending:** 295, Millionaire")
    elif "tools" in text or "🛠️" in message.text:
        bot.reply_to(message, "🛠️ **Tools:** Termux, Nmap")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    keep_alive()
    bot.infinity_polling()
import telebot
from telebot import types
import yt_dlp
import os
import time
from flask import Flask
from threading import Thread

# ==========================================
# 👇 AAPKI DETAILS (PRE-SET)
# ==========================================
API_TOKEN = '8552567148:AAFX7Pv2X0U3kVoZ-Ks4zxCytv-1r_DKPKQ'
ADMIN_ID = 5235560672
# ==========================================

bot = telebot.TeleBot(API_TOKEN)
app = Flask('')

@app.route('/')
def home():
    return "🚀 BOT IS ONLINE!"

def run_server():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    Thread(target=run_server).start()

def download_video_thread(message, url):
    chat_id = message.chat.id
    try:
        msg = bot.send_message(chat_id, "⏳ **Video dhoondh raha hu...**")
        filename = f"vid_{chat_id}.mp4"
        ydl_opts = {'format': 'best', 'outtmpl': filename, 'quiet': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        bot.edit_message_text("✅ **Uploading...**", chat_id, msg.message_id)
        with open(filename, 'rb') as video:
            bot.send_video(chat_id, video, caption=f"Lo Boss! 🔥")
        os.remove(filename)
    except Exception as e:
        bot.send_message(chat_id, "❌ Error: Link galat hai.")
        if os.path.exists(filename):
            os.remove(filename)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    name = message.from_user.first_name
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🎮 BGMI", "🎵 Songs", "🛠️ Tools")
    bot.reply_to(message, f"👋 **Namaste {name}!**\nBot taiyar hai. Link bhejo video ke liye.", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_all(message):
    text = message.text
    if "instagram.com" in text or "youtu" in text:
        Thread(target=download_video_thread, args=(message, text)).start()
    elif "BGMI" in text:
        bot.reply_to(message, "🔫 **BGMI Sens:** `7052-8888-0000`")
    elif "Songs" in text:
        bot.reply_to(message, "🎧 **Trending:** 295, Millionaire")
    elif "Tools" in text:
        bot.reply_to(message, "🛠️ **Tools:** Termux, Nmap")

if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling()
