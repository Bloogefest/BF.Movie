#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from typing import Union

import telebot.service_utils
from telebot.types import *

from str import *

class OldMenu:

    def __init__(self,
                 parent = None,
                 markup: ReplyKeyboardMarkup = None,
                 inline_markup: InlineKeyboardMarkup = None) -> None:
        self.parent = self if parent is None else parent
        self.markup = markup
        self.inline_markup = inline_markup
        self.inline = markup is None and inline_markup is not None

MENU_HOME_MARKUP = ReplyKeyboardMarkup(resize_keyboard = True)
MENU_HOME_MARKUP.add(KeyboardButton(STR_MENU_HOME_BTN_SEARCH))
MENU_HOME_MARKUP.add(KeyboardButton(STR_MENU_HOME_BTN_HELP),
                     KeyboardButton(STR_MENU_HOME_BTN_ABOUT))
MENU_HOME = OldMenu(markup = MENU_HOME_MARKUP)

MENU_SEARCH_MARKUP = ReplyKeyboardMarkup(resize_keyboard = True)
MENU_SEARCH_MARKUP.add(KeyboardButton(STR_MENU_SEARCH_BTN_CONFIRM))
MENU_SEARCH_MARKUP.add(KeyboardButton(STR_MENU_SEARCH_BTN_HOME),
                       KeyboardButton(STR_MENU_SEARCH_BTN_FILTERS))
MENU_SEARCH = OldMenu(parent = MENU_HOME,
                      markup = MENU_SEARCH_MARKUP)

MENU_SEARCH_RESULTS_MARKUP = InlineKeyboardMarkup()
MENU_SEARCH_RESULTS_MARKUP.add()
MENU_SEARCH_RESULTS = OldMenu(parent = MENU_SEARCH,
                              inline_markup = MENU_SEARCH_RESULTS_MARKUP)

MENU_SEARCH_FILTERS_MARKUP = ReplyKeyboardMarkup(resize_keyboard = True)
MENU_SEARCH_FILTERS_MARKUP.add(KeyboardButton(STR_MENU_SEARCH_FILTERS_BTN_MOVIE_TYPE),
                               KeyboardButton(STR_MENU_SEARCH_FILTERS_BTN_MOVIE_STATUS))
MENU_SEARCH_FILTERS_MARKUP.add(KeyboardButton(STR_MENU_SEARCH_FILTERS_BTN_PARENT),
                               KeyboardButton(STR_MENU_SEARCH_FILTERS_BTN_RESET))
MENU_SEARCH_FILTERS = OldMenu(parent = MENU_SEARCH,
                              markup = MENU_SEARCH_FILTERS_MARKUP)

MENU_SEARCH_FILTERS_MOVIE_TYPE_MARKUP = ReplyKeyboardMarkup(resize_keyboard = True)
MENU_SEARCH_FILTERS_MOVIE_TYPE_MARKUP.add(KeyboardButton(STR_MENU_SEARCH_FILTERS_MOVIE_TYPE_BTN_MOVIE),
                                          KeyboardButton(STR_MENU_SEARCH_FILTERS_MOVIE_TYPE_BTN_TV_SERIES))
MENU_SEARCH_FILTERS_MOVIE_TYPE_MARKUP.add(KeyboardButton(STR_MENU_SEARCH_FILTERS_MOVIE_TYPE_BTN_CARTOON),
                                          KeyboardButton(STR_MENU_SEARCH_FILTERS_MOVIE_TYPE_BTN_ANIME))
MENU_SEARCH_FILTERS_MOVIE_TYPE_MARKUP.add(KeyboardButton(STR_MENU_SEARCH_FILTERS_MOVIE_TYPE_BTN_ANIMATED_SERIES),
                                          KeyboardButton(STR_MENU_SEARCH_FILTERS_MOVIE_TYPE_BTN_TV_SHOW))
MENU_SEARCH_FILTERS_MOVIE_TYPE_MARKUP.add(KeyboardButton(STR_MENU_SEARCH_FILTERS_MOVIE_TYPE_BTN_PARENT),
                                          KeyboardButton(STR_MENU_SEARCH_FILTERS_MOVIE_TYPE_BTN_RESET))
MENU_SEARCH_FILTERS_MOVIE_TYPE = OldMenu(parent = MENU_SEARCH,
                                         markup = MENU_SEARCH_FILTERS_MOVIE_TYPE_MARKUP)

MENU_SEARCH_FILTERS_MOVIE_STATUS_MARKUP = ReplyKeyboardMarkup(resize_keyboard = True)
MENU_SEARCH_FILTERS_MOVIE_STATUS_MARKUP.add(KeyboardButton(STR_MENU_SEARCH_FILTERS_MOVIE_STATUS_BTN_FILMING),
                                            KeyboardButton(STR_MENU_SEARCH_FILTERS_MOVIE_STATUS_BTN_PRE_PRODUCTION))
MENU_SEARCH_FILTERS_MOVIE_STATUS_MARKUP.add(KeyboardButton(STR_MENU_SEARCH_FILTERS_MOVIE_STATUS_BTN_COMPLETED),
                                            KeyboardButton(STR_MENU_SEARCH_FILTERS_MOVIE_STATUS_BTN_ANNOUNCED))
MENU_SEARCH_FILTERS_MOVIE_STATUS_MARKUP.add(KeyboardButton(STR_MENU_SEARCH_FILTERS_MOVIE_STATUS_BTN_POST_PRODUCTION))
MENU_SEARCH_FILTERS_MOVIE_STATUS_MARKUP.add(KeyboardButton(STR_MENU_SEARCH_FILTERS_MOVIE_STATUS_BTN_PARENT),
                                            KeyboardButton(STR_MENU_SEARCH_FILTERS_MOVIE_STATUS_BTN_RESET))
MENU_SEARCH_FILTERS_MOVIE_STATUS = OldMenu(parent = MENU_SEARCH,
                                           markup = MENU_SEARCH_FILTERS_MOVIE_STATUS_MARKUP)

MENU_HELP_MARKUP = ReplyKeyboardMarkup(resize_keyboard = True)
MENU_HELP_MARKUP.add(KeyboardButton(STR_MENU_HELP_BTN_HOME))
MENU_HELP = OldMenu(parent = MENU_HOME,
                    markup = MENU_HELP_MARKUP)

MENU_ABOUT_MARKUP = ReplyKeyboardMarkup(resize_keyboard = True)
MENU_ABOUT_MARKUP.add(KeyboardButton(STR_MENU_ABOUT_BTN_HOME))
MENU_ABOUT = OldMenu(parent = MENU_HOME,
                     markup = MENU_ABOUT_MARKUP)

class Menu:

    def __init__(self,
                 schema: Union[str, tuple],
                 markup: Union[ReplyKeyboardMarkup, InlineKeyboardMarkup],
                 parent: Menu = None,
                 children: tuple[Menu] = None):
        self.schema = schema
        self.markup = markup
        self.parent = self if parent is None else parent
        self.children: tuple[Menu] = () if children is None else children

def menu_build_reply_schema_element(schema: dict[Union[str, dict], Union[function, None]],
                                    markup: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard = True)) -> ReplyKeyboardMarkup:
    for key, value in schema:
        if type(key) is str:
            markup.add(KeyboardButton(key))
        else:
            for element_ in element:
                markup.add(KeyboardButton(element_))
    return markup

def menu_build_reply_schema(schema: Union[str, dict],
                            markup: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard = True)) -> ReplyKeyboardMarkup:
    if type(schema) is str:
        markup.add(KeyboardButton(schema))
        return markup
    return menu_build_reply_schema_element(schema, markup)

def menu_build_inline_schema(schema: Union[str, tuple],
                             markup: InlineKeyboardMarkup = InlineKeyboardMarkup()) -> InlineKeyboardMarkup:
    if type(schema) is str:
        markup.add(KeyboardButton(schema))
        return markup
    for element in schema:
        if type(element) is str:
            markup.add(InlineKeyboardButton(element))
        else:
            for element_ in element:
                markup.add(InlineKeyboardButton(element_))
    return markup

MENU_INSTANCE_HOME = Menu(STR_MENU_SCHEMA_HOME,
                          menu_build_reply_markup(STR_MENU_SCHEMA_HOME))

MENU_INSTANCE_SEARCH = Menu(STR_MENU_SCHEMA_SEARCH,
                            menu_build_reply_markup(STR_MENU_SCHEMA_SEARCH))

MENU_INSTANCE_SEARCH_FILTERS = Menu(STR_MENU_SCHEMA_SEARCH_FILTERS,
                                    menu_build_reply_markup(STR_MENU_SCHEMA_SEARCH_FILTERS))

MENU_INSTANCE_SEARCH_FILTERS_TYPE = Menu(STR_MENU_SCHEMA_SEARCH_FILTERS_TYPE,
                                         menu_build_reply_markup(STR_MENU_SCHEMA_SEARCH_FILTERS_TYPE))

MENU_INSTANCE_SEARCH_FILTERS_STATUS = Menu(STR_MENU_SCHEMA_SEARCH_FILTERS_STATUS,
                                           menu_build_reply_markup(STR_MENU_SCHEMA_SEARCH_FILTERS_STATUS))

MENU_INSTANCE_HELP = Menu(STR_MENU_SCHEMA_HELP,
                          menu_build_reply_markup(STR_MENU_SCHEMA_HELP))

MENU_INSTANCE_ABOUT = Menu(STR_MENU_SCHEMA_ABOUT,
                           menu_build_reply_markup(STR_MENU_SCHEMA_ABOUT))
