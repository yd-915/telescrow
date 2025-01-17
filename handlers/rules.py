from config import *
from keyboard import *
from functions import *

@bot.message_handler(regexp="^Rules")
def rules(msg):
    """
    List of Rules
    """

    user = get_user(msg)
    try:
        message_id = get_msg_id(msg)
        bot.delete_message(user.chat, message_id)
    except:
        pass

    bot.send_message(
        user.id,
        emoji.emojize(
            f"""
:scroll: <b>TELEGRAM ESCROW BOT SERVICE RULES</b> :scroll:
----------------------------------------
1.  Trades can only be created by a seller.

2.  Funds deposited by the buyer are only released to seller after the goods received are affirmed by the buyer.

3.  Transaction price and trade currency should be agreed between both parties before trade is created.

4.  If a party is reported, the other party receives their refund and the guilty party banned from this service.
            """,
            
        ),
        parse_mode="html",
    )





@bot.message_handler(regexp="^Community")
def community(msg):
    """
    List of Community 
    """

    user = get_user(msg)
    try:
        message_id = get_msg_id(msg)
        bot.delete_message(user.chat, message_id)
    except:
        pass

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    a = types.InlineKeyboardButton(
        text="🌟 Bot Reviews", url="https://t.me/tele_escrowbot?message=start"
    )
    b = types.InlineKeyboardButton(
        text="🔄 Bot Updates", url="https://t.me/tele_escrowbot?message=start"
    )
    keyboard.add(a, b)

    bot.send_message(
        user.id,
        f"""
    🌐 <b>Explore Our Community!</b> 🌐

Stay updated 🔄 with the latest news updates and read what others are saying about us
        """,
        reply_markup=keyboard,
        parse_mode="html"
    )



