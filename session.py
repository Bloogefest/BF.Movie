#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from kp import *
from tg import *

class Session:

    def __init__(self, menu: Menu, search_filter_movie_type: KPTypeFilter = KPTypeFilter()):
        self.menu = menu
        self.search_filter_movie_type = search_filter_movie_type

SESSION_DICT = dict[int, Session]()

def session_get(user_id: int) -> Session:
    global SESSION_DICT
    if user_id in SESSION_DICT:
        return SESSION_DICT[user_id]
    session = SESSION_DICT[user_id] = Session(MENU_HOME)
    return session

def session_menu_get(user_id: int) -> Menu:
    return session_get(user_id).menu

def session_menu_set(user_id: int, menu: Menu) -> None:
    session_get(user_id).menu = menu
