#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from session import *

class Menu:

    def __init__(self, parent = None, markup: ReplyKeyboardMarkup = None) -> None:
        self.parent = self if parent is None else parent
        self.markup = markup

MENU_HOME_MARKUP = ReplyKeyboardMarkup(resize_keyboard = True)
MENU_HOME_MARKUP.add(KeyboardButton(STR_MENU_HOME_BTN_SEARCH))
MENU_HOME_MARKUP.add(KeyboardButton(STR_MENU_HOME_BTN_HELP), KeyboardButton(STR_MENU_HOME_BTN_ABOUT))
MENU_HOME = Menu(markup = MENU_HOME_MARKUP)

MENU_SEARCH_MARKUP = ReplyKeyboardMarkup(resize_keyboard = True)
MENU_SEARCH_MARKUP.add(KeyboardButton(STR_MENU_SEARCH_BTN_CONFIRM))
MENU_SEARCH_MARKUP.add(KeyboardButton(STR_MENU_SEARCH_BTN_HOME), KeyboardButton(STR_MENU_SEARCH_BTN_FILTERS))
MENU_SEARCH = Menu(parent = MENU_HOME, markup = MENU_SEARCH_MARKUP)

MENU_SEARCH_FILTERS_MARKUP = ReplyKeyboardMarkup(resize_keyboard = True)
MENU_SEARCH_FILTERS_MARKUP.add(KeyboardButton(STR_MENU_SEARCH_FILTERS_BTN_MOVIE_TYPE))
MENU_SEARCH_FILTERS_MARKUP.add(KeyboardButton(STR_MENU_SEARCH_FILTERS_BTN_PARENT), KeyboardButton(STR_MENU_SEARCH_FILTERS_BTN_RESET))
MENU_SEARCH_FILTERS = Menu(parent = MENU_SEARCH, markup = MENU_SEARCH_FILTERS_MARKUP)

MENU_SEARCH_FILTERS_MOVIE_TYPE_MARKUP = ReplyKeyboardMarkup(resize_keyboard = True)
MENU_SEARCH_FILTERS_MOVIE_TYPE_MARKUP.add(KeyboardButton(STR_MENU_SEARCH_FILTERS_MOVIE_TYPE_BTN_MOVIE), KeyboardButton(STR_MENU_SEARCH_FILTERS_MOVIE_TYPE_BTN_TV_SERIES))
MENU_SEARCH_FILTERS_MOVIE_TYPE_MARKUP.add(KeyboardButton(STR_MENU_SEARCH_FILTERS_MOVIE_TYPE_BTN_CARTOON), KeyboardButton(STR_MENU_SEARCH_FILTERS_MOVIE_TYPE_BTN_ANIME))
MENU_SEARCH_FILTERS_MOVIE_TYPE_MARKUP.add(KeyboardButton(STR_MENU_SEARCH_FILTERS_MOVIE_TYPE_BTN_ANIMATED_SERIES), KeyboardButton(STR_MENU_SEARCH_FILTERS_MOVIE_TYPE_BTN_TV_SHOW))
MENU_SEARCH_FILTERS_MOVIE_TYPE_MARKUP.add(KeyboardButton(STR_MENU_SEARCH_FILTERS_MOVIE_TYPE_BTN_PARENT), KeyboardButton(STR_MENU_SEARCH_FILTERS_MOVIE_TYPE_BTN_RESET))
MENU_SEARCH_FILTERS_MOVIE_TYPE = Menu(parent = MENU_SEARCH, markup = MENU_SEARCH_FILTERS_MOVIE_TYPE_MARKUP)

MENU_HELP_MARKUP = ReplyKeyboardMarkup(resize_keyboard = True)
MENU_HELP_MARKUP.add(KeyboardButton(STR_MENU_HELP_BTN_HOME))
MENU_HELP = Menu(parent = MENU_HOME, markup = MENU_HELP_MARKUP)

MENU_ABOUT_MARKUP = ReplyKeyboardMarkup(resize_keyboard = True)
MENU_ABOUT_MARKUP.add(KeyboardButton(STR_MENU_ABOUT_BTN_HOME))
MENU_ABOUT = Menu(parent = MENU_HOME, markup = MENU_ABOUT_MARKUP)
