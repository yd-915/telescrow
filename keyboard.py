from config import *


def main_menu(msg):
    "Return Main Menu Keyboard"

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    a = types.InlineKeyboardButton(text=emoji.emojize("I am a Seller :man:", use_aliases=True), callback_data="seller")
    b = types.InlineKeyboardButton(text=emoji.emojize("I am a Buyer :man:", use_aliases=True), callback_data="buyer")
    c = types.InlineKeyboardButton(text=emoji.emojize(":man: Using this service on my group :man:", use_aliases=True), callback_data="affiliate")
    
    keyboard.add(a,b)
    
    if msg.chat.type == "private":
        keyboard.add(c)
    
    return keyboard


def seller_menu():
    "Return Seller Options"

    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    a = types.KeyboardButton(emoji.emojize("Initiate Trade :ledger:", use_aliases=True))
    b = types.KeyboardButton(emoji.emojize("Delete Trade :closed_book:", use_aliases=True))
    c = types.KeyboardButton(emoji.emojize("Trade History :books:", use_aliases=True))
    d = types.KeyboardButton(emoji.emojize("Rules :scroll:", use_aliases=True))

    keyboard.add(a,b,c,d)
    return keyboard


def buyer_menu():
    "Return Buyer Options"

    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    a = types.KeyboardButton(emoji.emojize("Join Trade :memo:", use_aliases=True))
    b = types.KeyboardButton(emoji.emojize("Report Trade :open_file_folder:", use_aliases=True))
    c = types.KeyboardButton(emoji.emojize("Trade History :books:", use_aliases=True))
    d = types.KeyboardButton(emoji.emojize("Rules :scroll:", use_aliases=True))

    keyboard.add(a,b,c,d)
    return keyboard

def agent_menu(balance):
    "Return Agent Options"
    
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    a = types.InlineKeyboardButton(text=emoji.emojize("Deposit  :inbox_tray:", use_aliases=True), callback_data="deposit")
    b = types.InlineKeyboardButton(text=emoji.emojize(f"Balance {balance}BTC  :moneybag:", use_aliases=True), callback_data="d")
    c = types.InlineKeyboardButton(text=emoji.emojize("Withdraw  :outbox_tray:", use_aliases=True), callback_data="withdraw")
    d = types.InlineKeyboardButton(text=emoji.emojize("Help  :bulb:", use_aliases=True), callback_data="help")
    e = types.InlineKeyboardButton(text=emoji.emojize("History  :book:", use_aliases=True), callback_data="agent_trades")
    f = types.InlineKeyboardButton(text=emoji.emojize(":man: Add Bot To Your Group", use_aliases=True), callback_data="affiliate")

    keyboard.add(a,b,c,d,e,f)
    return keyboard

def local_currency_menu():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    a = types.InlineKeyboardButton(text=emoji.emojize(":dollar: US Dollars (USD)", use_aliases=True), callback_data="dollar")
    b = types.InlineKeyboardButton(text=emoji.emojize(":euro: Euros (EUR)", use_aliases=True), callback_data="euro")
    
    keyboard.add(a,b)
    return keyboard


def coin_menu():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    a = types.InlineKeyboardButton(text=emoji.emojize("Bitcoin (BTC)", use_aliases=True), callback_data="btc")
    b = types.InlineKeyboardButton(text=emoji.emojize("Ethereum (ETH)", use_aliases=True), callback_data="eth")
    
    keyboard.add(a,b)
    return keyboard

def give_verdict():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    a = types.InlineKeyboardButton(text=emoji.emojize("Yes :+1:", use_aliases=True), callback_data="verdict")
    b = types.InlineKeyboardButton(text=emoji.emojize("No :-1:", use_aliases=True), callback_data="2")
    
    keyboard.add(a,b)
    return keyboard

def confirm():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    a = types.InlineKeyboardButton(text=emoji.emojize(":money_bag: Confirm Payment", use_aliases=True), callback_data="payment_confirmation")
    keyboard.add(a)
    return keyboard

def confirm_goods():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    a = types.InlineKeyboardButton(text=emoji.emojize("Received :white_check_mark:", use_aliases=True), callback_data="goods_received")
    b = types.InlineKeyboardButton(text=emoji.emojize("Not Received :x:", use_aliases=True), callback_data="goods_not_received")
    keyboard.add(a, b)
    return keyboard

def refunds():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    a = types.InlineKeyboardButton(text=emoji.emojize(":man: To Buyer", use_aliases=True), callback_data="refund_to_buyer")
    b = types.InlineKeyboardButton(text=emoji.emojize(":man: To Seller", use_aliases=True), callback_data="pay_to_seller")
    c = types.InlineKeyboardButton(text=emoji.emojize(" :closed_lock_with_key: Close Trade", use_aliases=True), callback_data="close_trade")
    keyboard.add(a, b, c)
    return keyboard


def select_trade():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    a = types.InlineKeyboardButton(text=emoji.emojize("View Trades", use_aliases=True), callback_data="view_all_trades")
    b = types.InlineKeyboardButton(text=emoji.emojize("Delete Trade", use_aliases=True), callback_data="delete_trade")
    keyboard.add(a, b)
    return keyboard