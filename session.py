#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from typing import Union

from telebot.types import *

from kp import *
from tg import *
from menu import *

class OldSession:

    def __init__(self,
                 menu: OldMenu,
                 search_filter_movie_type: KPTypeFilter = KPTypeFilter(),
                 search_filter_movie_status: KPStatusFilter = KPStatusFilter()):
        self.menu = menu
        self.search_filter_movie_type = search_filter_movie_type
        self.search_filter_movie_status = search_filter_movie_status

SESSION_DICT = dict[int, OldSession]()

def session_get(user_id: int) -> OldSession:
    global SESSION_DICT
    if user_id in SESSION_DICT:
        return SESSION_DICT[user_id]
    session = SESSION_DICT[user_id] = OldSession(MENU_HOME)
    return session

def session_menu_get(user_id: int) -> OldMenu:
    return session_get(user_id).menu

def session_menu_set(user_id: int,
                     menu: OldMenu) -> None:
    session_get(user_id).menu = menu

class Session:
    def __init__(self,
                 uid: int,
                 menu: Menu = MENU_INSTANCE_HOME):
        self.uid = uid
        self.menu = menu

SESSION_INSTANCE_STORAGE: dict[int, Session] = { }

def session_instance_restore(uid: int) -> Session:
    global SESSION_INSTANCE_STORAGE
    if uid in SESSION_INSTANCE_STORAGE:
        return SESSION_INSTANCE_STORAGE[uid]
    session = SESSION_INSTANCE_STORAGE[uid] = Session(uid)
    return session

def session_instance_store(session: Session) -> bool:
    global SESSION_INSTANCE_STORAGE
    if session.uid in SESSION_INSTANCE_STORAGE:
        return False
    SESSION_INSTANCE_STORAGE[uid] = session
    return True

def session_instance_stored(uid: int) -> bool:
    global SESSION_INSTANCE_STORAGE
    return uid in SESSION_INSTANCE_STORAGE

def session_instance_delete(uid: int) -> bool:
    global SESSION_INSTANCE_STORAGE
    if session.uid in SESSION_INSTANCE_STORAGE:
        SESSION_INSTANCE_STORAGE.pop(session.uid)
        return True
    return False
