#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from telebot.types import User

from cfg import *

def wl_check(user: User) -> bool:
    if not CFG_WL:
        return True
    if user.is_bot and not CFG_WL_ALLOW_BOTS:
        return False
    return user.id in cfg_wl_src()
