from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def get_main_menu():
    keyboard = [
        [InlineKeyboardButton("Generate Config", callback_data="generate")],
        [InlineKeyboardButton("My Configs", callback_data="configs")]
    ]
    return InlineKeyboardMarkup(keyboard)
