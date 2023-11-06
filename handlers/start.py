from config import *
from keyboard import *
from functions import *

@bot.message_handler(commands=['start', 'escrow'])
def start(msg):
    """
    Starting the escrow service bot
    """
    print(f"New User - {msg.from_user.username} - {msg.from_user.id}")
    keyboard = main_menu(msg)

    bot.reply_to(
        msg,
        emoji.emojize(
            f"""
    Hello {msg.from_user.first_name},

    :circus_tent: Welcome to the Telegram Escrow Service Bot. My purpose is to create a save trade environment for both seller and buyer subject to my rules.

    Your funds are save with me and will be refunded to you if the other party refuses to comply with the rules.
    
    What would be your role today?
            """
        ),
        reply_markup=keyboard
    )


