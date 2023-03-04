#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from telebot import *
from telebot.async_telebot import *
from asyncio import run

from cfg import *
from str import *
from msg import *
from log import *
from wl import *
from session import *
from menu import *

TG_INSTANCE: AsyncTeleBot

class TGExceptionHandler(ExceptionHandler):

    def handle(self, e: BaseException):
        log_get_logger("tg").exception(e.__str__())

def tg_get_instance() -> AsyncTeleBot:
    global TG_INSTANCE
    if "TG_INSTANCE" in globals():
        return TG_INSTANCE
    TG_INSTANCE = AsyncTeleBot(cfg_tg_tkn_src(), exception_handler = TGExceptionHandler())
    return TG_INSTANCE

def tg_launch() -> None:
    run(tg_get_instance().polling(), debug = CFG_BOT_IN_DEVELOPMENT)

def tg_check_message(message: Message, *signatures: str, menu: Menu = None) -> bool:
    return (menu is None or session_menu_get(message.from_user.id) is menu) and tg_check_signature(message, signatures)

async def tg_check_wl(message: Message) -> bool:
    if wl_check(message.from_user):
        return True
    await tg_reply_message(message, MSG_WL_NOT_LISTED)
    return False

def tg_check_signature(message: Message, signatures: tuple[str]) -> bool:
    return message.text in signatures

def tg_handle_message(message: Message) -> None:
    log_get_logger("tg").debug(f"[ID/{message.from_user.id}] [Name/{message.from_user.first_name}{'' if message.from_user.last_name is None else ' ' + message.from_user.last_name}] {message.text}")

async def tg_reply_message(message: Message, text: str) -> None:
    await TG_INSTANCE.reply_to(message, text, reply_markup = session_menu_get(message.from_user.id).markup)

@tg_get_instance().message_handler(func = lambda message: tg_check_message(message, STR_CMD_START))
async def start(message: Message) -> None:
    if not await tg_check_wl(message):
        return
    session_menu_set(message.from_user.id, MENU_HOME)
    tg_handle_message(message)
    await tg_reply_message(message, MSG_CMD_START)

@tg_get_instance().message_handler(func = lambda message: tg_check_message(message, STR_CMD_HOME, STR_MENU_SEARCH_BTN_HOME, STR_MENU_HELP_BTN_HOME, STR_MENU_ABOUT_BTN_HOME))
async def home(message: Message) -> None:
    if not await tg_check_wl(message):
        return
    session_menu_set(message.from_user.id, MENU_HOME)
    await tg_reply_message(message, MSG_CMD_HOME)

@tg_get_instance().message_handler(func = lambda message: tg_check_message(message, STR_CMD_SEARCH, STR_MENU_HOME_BTN_SEARCH, STR_MENU_SEARCH_FILTERS_BTN_PARENT))
async def search(message: Message) -> None:
    if not await tg_check_wl(message):
        return
    session_menu_set(message.from_user.id, MENU_SEARCH)
    tg_handle_message(message)
    await tg_reply_message(message, MSG_CMD_SEARCH)

@tg_get_instance().message_handler(func = lambda message: tg_check_message(message, STR_CMD_SEARCH_CONFIRM, STR_MENU_SEARCH_BTN_CONFIRM))
async def search_confirm(message: Message) -> None:
    if not await tg_check_wl(message):
        return
    tg_handle_message(message)
    await tg_reply_message(message, MSG_CMD_SEARCH_CONFIRM)

@tg_get_instance().message_handler(func = lambda message: tg_check_message(message, STR_CMD_SEARCH_FILTERS, STR_MENU_SEARCH_BTN_FILTERS, STR_MENU_SEARCH_FILTERS_MOVIE_TYPE_BTN_PARENT, STR_MENU_SEARCH_FILTERS_MOVIE_STATUS_BTN_PARENT))
async def search_filters(message: Message) -> None:
    if not await tg_check_wl(message):
        return
    session_menu_set(message.from_user.id, MENU_SEARCH_FILTERS)
    tg_handle_message(message)
    await tg_reply_message(message, MSG_CMD_SEARCH_FILTERS)

# SEARCH FILTER MOVIE TYPE MENU #

@tg_get_instance().message_handler(func = lambda message: tg_check_message(message, STR_CMD_SEARCH_FILTERS_MOVIE_TYPE, STR_MENU_SEARCH_FILTERS_BTN_MOVIE_TYPE))
async def search_filters_movie_type(message: Message) -> None:
    if not await tg_check_wl(message):
        return
    session_menu_set(message.from_user.id, MENU_SEARCH_FILTERS_MOVIE_TYPE)
    tg_handle_message(message)
    await tg_reply_message(message, msg_get_cmd_search_filters_movie_type(session_get(message.from_user.id)))

@tg_get_instance().message_handler(func = lambda message: tg_check_message(message, STR_CMD_SEARCH_FILTERS_MOVIE_TYPE_MOVIE, STR_MENU_SEARCH_FILTERS_MOVIE_TYPE_BTN_MOVIE))
async def movie_type_movie(message: Message) -> None:
    if not await tg_check_wl(message):
        return
    tg_handle_message(message)
    session_get(message.from_user.id).search_filter_movie_type.handle_type(KPMovieType.MOVIE)
    await tg_reply_message(message, msg_get_cmd_search_filters_movie_type(session_get(message.from_user.id)))

@tg_get_instance().message_handler(func = lambda message: tg_check_message(message, STR_CMD_SEARCH_FILTERS_MOVIE_TYPE_TV_SERIES, STR_MENU_SEARCH_FILTERS_MOVIE_TYPE_BTN_TV_SERIES))
async def movie_type_tv_series(message: Message) -> None:
    if not await tg_check_wl(message):
        return
    tg_handle_message(message)
    session_get(message.from_user.id).search_filter_movie_type.handle_type(KPMovieType.TV_SERIES)
    await tg_reply_message(message, msg_get_cmd_search_filters_movie_type(session_get(message.from_user.id)))

@tg_get_instance().message_handler(func = lambda message: tg_check_message(message, STR_CMD_SEARCH_FILTERS_MOVIE_TYPE_CARTOON, STR_MENU_SEARCH_FILTERS_MOVIE_TYPE_BTN_CARTOON))
async def movie_type_cartoon(message: Message) -> None:
    if not await tg_check_wl(message):
        return
    tg_handle_message(message)
    session_get(message.from_user.id).search_filter_movie_type.handle_type(KPMovieType.CARTOON)
    await tg_reply_message(message, msg_get_cmd_search_filters_movie_type(session_get(message.from_user.id)))

@tg_get_instance().message_handler(func = lambda message: tg_check_message(message, STR_CMD_SEARCH_FILTERS_MOVIE_TYPE_ANIME, STR_MENU_SEARCH_FILTERS_MOVIE_TYPE_BTN_ANIME))
async def movie_type_anime(message: Message) -> None:
    if not await tg_check_wl(message):
        return
    tg_handle_message(message)
    session_get(message.from_user.id).search_filter_movie_type.handle_type(KPMovieType.ANIME)
    await tg_reply_message(message, msg_get_cmd_search_filters_movie_type(session_get(message.from_user.id)))

@tg_get_instance().message_handler(func = lambda message: tg_check_message(message, STR_CMD_SEARCH_FILTERS_MOVIE_TYPE_ANIMATED_SERIES, STR_MENU_SEARCH_FILTERS_MOVIE_TYPE_BTN_ANIMATED_SERIES))
async def movie_type_animated_series(message: Message) -> None:
    if not await tg_check_wl(message):
        return
    tg_handle_message(message)
    session_get(message.from_user.id).search_filter_movie_type.handle_type(KPMovieType.ANIMATED_SERIES)
    await tg_reply_message(message, msg_get_cmd_search_filters_movie_type(session_get(message.from_user.id)))

@tg_get_instance().message_handler(func = lambda message: tg_check_message(message, STR_CMD_SEARCH_FILTERS_MOVIE_TYPE_TV_SHOW, STR_MENU_SEARCH_FILTERS_MOVIE_TYPE_BTN_TV_SHOW))
async def movie_type_tv_show(message: Message) -> None:
    if not await tg_check_wl(message):
        return
    tg_handle_message(message)
    session_get(message.from_user.id).search_filter_movie_type.handle_type(KPMovieType.TV_SHOW)
    await tg_reply_message(message, msg_get_cmd_search_filters_movie_type(session_get(message.from_user.id)))

@tg_get_instance().message_handler(func = lambda message: tg_check_message(message, STR_CMD_SEARCH_FILTERS_MOVIE_TYPE_RESET, STR_MENU_SEARCH_FILTERS_MOVIE_TYPE_BTN_RESET, menu = MENU_SEARCH_FILTERS_MOVIE_TYPE))
async def search_filters_movie_type_reset(message: Message) -> None:
    if not await tg_check_wl(message):
        return
    tg_handle_message(message)
    session_get(message.from_user.id).search_filter_movie_type.clear()
    await tg_reply_message(message, msg_get_cmd_search_filters_movie_type(session_get(message.from_user.id)))

# SEARCH FILTER MOVIE TYPE MENU #

# SEARCH FILTER MOVIE STATUS MENU #

@tg_get_instance().message_handler(func = lambda message: tg_check_message(message, STR_CMD_SEARCH_FILTERS_MOVIE_STATUS, STR_MENU_SEARCH_FILTERS_BTN_MOVIE_STATUS))
async def search_filters_movie_status(message: Message) -> None:
    if not await tg_check_wl(message):
        return
    session_menu_set(message.from_user.id, MENU_SEARCH_FILTERS_MOVIE_STATUS)
    tg_handle_message(message)
    await tg_reply_message(message, msg_get_cmd_search_filters_movie_status(session_get(message.from_user.id)))

@tg_get_instance().message_handler(func = lambda message: tg_check_message(message, STR_CMD_SEARCH_FILTERS_MOVIE_STATUS_FILMING, STR_MENU_SEARCH_FILTERS_MOVIE_STATUS_BTN_FILMING))
async def movie_status_filming(message: Message) -> None:
    if not await tg_check_wl(message):
        return
    tg_handle_message(message)
    session_get(message.from_user.id).search_filter_movie_status.handle_type(KPMovieStatus.FILMING)
    await tg_reply_message(message, msg_get_cmd_search_filters_movie_status(session_get(message.from_user.id)))

@tg_get_instance().message_handler(func = lambda message: tg_check_message(message, STR_CMD_SEARCH_FILTERS_MOVIE_STATUS_PRE_PRODUCTION, STR_MENU_SEARCH_FILTERS_MOVIE_STATUS_BTN_PRE_PRODUCTION))
async def movie_status_pre_production(message: Message) -> None:
    if not await tg_check_wl(message):
        return
    tg_handle_message(message)
    session_get(message.from_user.id).search_filter_movie_status.handle_type(KPMovieStatus.PRE_PRODUCTION)
    await tg_reply_message(message, msg_get_cmd_search_filters_movie_status(session_get(message.from_user.id)))

@tg_get_instance().message_handler(func = lambda message: tg_check_message(message, STR_CMD_SEARCH_FILTERS_MOVIE_STATUS_COMPLETED, STR_MENU_SEARCH_FILTERS_MOVIE_STATUS_BTN_COMPLETED))
async def movie_status_completed(message: Message) -> None:
    if not await tg_check_wl(message):
        return
    tg_handle_message(message)
    session_get(message.from_user.id).search_filter_movie_status.handle_type(KPMovieStatus.COMPLETED)
    await tg_reply_message(message, msg_get_cmd_search_filters_movie_status(session_get(message.from_user.id)))

@tg_get_instance().message_handler(func = lambda message: tg_check_message(message, STR_CMD_SEARCH_FILTERS_MOVIE_STATUS_ANNOUNCED, STR_MENU_SEARCH_FILTERS_MOVIE_STATUS_BTN_ANNOUNCED))
async def movie_status_announced(message: Message) -> None:
    if not await tg_check_wl(message):
        return
    tg_handle_message(message)
    session_get(message.from_user.id).search_filter_movie_status.handle_type(KPMovieStatus.ANNOUNCED)
    await tg_reply_message(message, msg_get_cmd_search_filters_movie_status(session_get(message.from_user.id)))

@tg_get_instance().message_handler(func = lambda message: tg_check_message(message, STR_CMD_SEARCH_FILTERS_MOVIE_STATUS_POST_PRODUCTION, STR_MENU_SEARCH_FILTERS_MOVIE_STATUS_BTN_POST_PRODUCTION))
async def movie_status_post_production(message: Message) -> None:
    if not await tg_check_wl(message):
        return
    tg_handle_message(message)
    session_get(message.from_user.id).search_filter_movie_status.handle_type(KPMovieStatus.POST_PRODUCTION)
    await tg_reply_message(message, msg_get_cmd_search_filters_movie_status(session_get(message.from_user.id)))

@tg_get_instance().message_handler(func = lambda message: tg_check_message(message, STR_CMD_SEARCH_FILTERS_MOVIE_STATUS_RESET, STR_MENU_SEARCH_FILTERS_MOVIE_STATUS_BTN_RESET, menu = MENU_SEARCH_FILTERS_MOVIE_STATUS))
async def search_filters_movie_status_reset(message: Message) -> None:
    if not await tg_check_wl(message):
        return
    tg_handle_message(message)
    session_get(message.from_user.id).search_filter_movie_status.clear()
    await tg_reply_message(message, msg_get_cmd_search_filters_movie_status(session_get(message.from_user.id)))

# SEARCH FILTER MOVIE STATUS MENU #

@tg_get_instance().message_handler(func = lambda message: tg_check_message(message, STR_CMD_SEARCH_FILTERS_RESET, STR_MENU_SEARCH_FILTERS_BTN_RESET, menu = MENU_SEARCH_FILTERS))
async def search_filters_reset(message: Message) -> None:
    if not await tg_check_wl(message):
        return
    tg_handle_message(message)
    session_get(message.from_user.id).search_filter_movie_type.clear()
    await tg_reply_message(message, MSG_CMD_SEARCH_FILTERS_RESET)

@tg_get_instance().message_handler(func = lambda message: tg_check_message(message, STR_CMD_HELP, STR_MENU_HOME_BTN_HELP))
async def help_(message: Message) -> None:
    if not await tg_check_wl(message):
        return
    session_menu_set(message.from_user.id, MENU_HELP)
    tg_handle_message(message)
    await tg_reply_message(message, MSG_CMD_HELP)

@tg_get_instance().message_handler(func = lambda message: tg_check_message(message, STR_CMD_ABOUT, STR_MENU_HOME_BTN_ABOUT))
async def about(message: Message) -> None:
    if not await tg_check_wl(message):
        return
    session_menu_set(message.from_user.id, MENU_ABOUT)
    tg_handle_message(message)
    await tg_reply_message(message, MSG_CMD_ABOUT)
