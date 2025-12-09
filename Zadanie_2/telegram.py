import telebot
import os

bot = telebot.TeleBot('8247592116:AAGqqaPxcDHwfVDk2nnDTbG6zCovZssMCso')
file_path = 'Задание 2/message.txt'

chat_id = '1121163791'

def send_message_to_telegram(chat_id, message):
    bot.send_message(chat_id, message)

if __name__ == "__main__":
    if not os.path.exists(file_path):
        print(f"Файл не найден: {file_path}")
    else:
        with open(file_path, 'r', encoding='utf-8') as file:
            message = file.read()

        send_message_to_telegram(chat_id, message)
        print("Сообщение успешно отправлено!")

    bot.infinity_polling()
