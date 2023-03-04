#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from asyncio import *

from telebot.types import *
from telebot.async_telebot import *

from cfg import *
from str import *
from msg import *
from log import *
from wl import *

TG_INSTANCE: AsyncTeleBot

class TGMenu:

    def __init__(self, parent = None, markup: ReplyKeyboardMarkup = None):
        self.parent = self if parent is None else parent
        self.markup = markup

TG_MENU_HOME_MARKUP = ReplyKeyboardMarkup(resize_keyboard = True)
TG_MENU_HOME_MARKUP.add(KeyboardButton(STR_MENU_HOME_BTN_SEARCH))
TG_MENU_HOME_MARKUP.add(KeyboardButton(STR_MENU_HOME_BTN_HELP), KeyboardButton(STR_MENU_HOME_BTN_ABOUT))
TG_MENU_HOME = TGMenu(markup = TG_MENU_HOME_MARKUP)

TG_MENU_SEARCH_MARKUP = ReplyKeyboardMarkup(resize_keyboard = True)
TG_MENU_SEARCH_MARKUP.add(KeyboardButton(STR_MENU_SEARCH_BTN_CONFIRM))
TG_MENU_SEARCH_MARKUP.add(KeyboardButton(STR_MENU_SEARCH_BTN_HOME), KeyboardButton(STR_MENU_SEARCH_BTN_FILTERS))
TG_MENU_SEARCH = TGMenu(parent = TG_MENU_HOME, markup = TG_MENU_SEARCH_MARKUP)

TG_MENU_SEARCH_FILTERS_MARKUP = ReplyKeyboardMarkup(resize_keyboard = True)
TG_MENU_SEARCH_FILTERS_MARKUP.add(KeyboardButton(STR_MENU_SEARCH_FILTERS_BTN_PARENT), KeyboardButton(STR_MENU_SEARCH_FILTERS_BTN_RESET))
TG_MENU_SEARCH_FILTERS = TGMenu(parent = TG_MENU_SEARCH, markup = TG_MENU_SEARCH_FILTERS_MARKUP)

TG_MENU_HELP_MARKUP = ReplyKeyboardMarkup(resize_keyboard = True)
TG_MENU_HELP_MARKUP.add(KeyboardButton(STR_MENU_HELP_BTN_HOME))
TG_MENU_HELP = TGMenu(parent = TG_MENU_HOME, markup = TG_MENU_HELP_MARKUP)

TG_MENU_ABOUT_MARKUP = ReplyKeyboardMarkup(resize_keyboard = True)
TG_MENU_ABOUT_MARKUP.add(KeyboardButton(STR_MENU_ABOUT_BTN_HOME))
TG_MENU_ABOUT = TGMenu(parent = TG_MENU_HOME, markup = TG_MENU_ABOUT_MARKUP)

TG_CURRENT_MENU = TG_MENU_HOME

def tg_get_instance() -> AsyncTeleBot:
    global TG_INSTANCE
    if "TG_INSTANCE" in globals():
        return TG_INSTANCE
    TG_INSTANCE = AsyncTeleBot(cfg_tg_tkn_src())
    return TG_INSTANCE

def tg_launch() -> None:
    run(tg_get_instance().polling(), debug = CFG_BOT_IN_DEVELOPMENT)

def tg_check_message(message: Message, *signatures: str) -> bool:
    return wl_check(message.from_user) and tg_check_signature(message, signatures)

def tg_check_signature(message: Message, signatures: tuple[str]) -> bool:
    return message.text in signatures

def tg_set_menu(menu: TGMenu) -> None:
    global TG_CURRENT_MENU
    TG_CURRENT_MENU = menu

def tg_handle_message(message: Message) -> None:
    log_get_logger("tg").debug(f"[ID/{message.from_user.id}] [Name/{message.from_user.first_name}{'' if message.from_user.last_name is None else ' ' + message.from_user.last_name}] {message.text}")

async def tg_reply_message(message: Message, text: str) -> None:
    await TG_INSTANCE.reply_to(message, text, reply_markup = TG_CURRENT_MENU.markup)

@tg_get_instance().message_handler(func=lambda message: tg_check_message(message, STR_CMD_START))
async def start(message: Message) -> None:
    tg_set_menu(TG_MENU_HOME)
    tg_handle_message(message)
    await tg_reply_message(message, MSG_CMD_START)

@tg_get_instance().message_handler(func=lambda message: tg_check_message(message, STR_CMD_HOME, STR_MENU_SEARCH_BTN_HOME, STR_MENU_HELP_BTN_HOME, STR_MENU_ABOUT_BTN_HOME))
async def home(message: Message) -> None:
    tg_set_menu(TG_MENU_HOME)
    await tg_reply_message(message, MSG_CMD_HOME)

@tg_get_instance().message_handler(func=lambda message: tg_check_message(message, STR_CMD_SEARCH, STR_MENU_HOME_BTN_SEARCH, STR_MENU_SEARCH_FILTERS_BTN_PARENT))
async def search(message: Message) -> None:
    tg_set_menu(TG_MENU_SEARCH)
    tg_handle_message(message)
    await tg_reply_message(message, MSG_CMD_SEARCH)

@tg_get_instance().message_handler(func=lambda message: tg_check_message(message, STR_CMD_SEARCH_CONFIRM, STR_MENU_SEARCH_BTN_CONFIRM))
async def search_confirm(message: Message) -> None:
    tg_handle_message(message)
    await tg_reply_message(message, MSG_CMD_SEARCH_CONFIRM)

@tg_get_instance().message_handler(func=lambda message: tg_check_message(message, STR_CMD_SEARCH_FILTERS, STR_MENU_SEARCH_BTN_FILTERS))
async def search_filters(message: Message) -> None:
    tg_set_menu(TG_MENU_SEARCH_FILTERS)
    tg_handle_message(message)
    await tg_reply_message(message, MSG_CMD_SEARCH_FILTERS)

@tg_get_instance().message_handler(func=lambda message: tg_check_message(message, STR_CMD_SEARCH_FILTERS_RESET, STR_MENU_SEARCH_FILTERS_BTN_RESET))
async def search_filters_reset(message: Message) -> None:
    tg_handle_message(message)
    await tg_reply_message(message, MSG_CMD_SEARCH_FILTERS_RESET)

@tg_get_instance().message_handler(func=lambda message: tg_check_message(message, STR_CMD_HELP, STR_MENU_HOME_BTN_HELP))
async def help_(message: Message) -> None:
    tg_set_menu(TG_MENU_HELP)
    tg_handle_message(message)
    await tg_reply_message(message, MSG_CMD_HELP)

@tg_get_instance().message_handler(func=lambda message: tg_check_message(message, STR_CMD_ABOUT, STR_MENU_HOME_BTN_ABOUT))
async def about(message: Message) -> None:
    tg_set_menu(TG_MENU_ABOUT)
    tg_handle_message(message)
    await tg_reply_message(message, MSG_CMD_ABOUT)
