#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from logging import *

# CFG_BOT

CFG_BOT_ID = "bf_movie_bot"
CFG_BOT_NAME = "BF.Movie"
CFG_BOT_VERSION = "1.0"

CFG_BOT_IN_DEVELOPMENT = True

# CFG_WL

CFG_WL = True

CFG_WL_ALLOW_BOTS = False

CFG_WL_SRC: list[int]

CFG_WL_PATH = "wl.txt"
CFG_WL_MODE = "r"
CFG_WL_ENCODING = "UTF-8"

# CFG_TG

CFG_TG_TKN_SRC: str

CFG_TG_TKN_PATH = "tg.tkn"
CFG_TG_TKN_MODE = "r"
CFG_TG_TKN_ENCODING = "UTF-8"

# CFG_KP

CFG_KP_TKN_SRC: str

CFG_KP_TKN_PATH = "kp.tkn"
CFG_KP_TKN_MODE = "r"
CFG_KP_TKN_ENCODING = "UTF-8"

# CFG_LOG

CFG_LOG_LVL: int

CFG_LOG_SETUP_CONSOLE = True

CFG_LOG_MODE = "a"
CFG_LOG_ENCODING = "UTF-8"
CFG_LOG_MAX_BYTES = 1024 * 1024 * 1024
CFG_LOG_BACKUP_COUNT = 2

CFG_LOG_PRODUCTION_LVL = WARNING
CFG_LOG_IN_DEVELOPMENT_LVL = DEBUG

CFG_LOG_PARENT_PATH = "logs/"
CFG_LOG_PATH_PREFIX = ""
CFG_LOG_PATH_SUFFIX = ".txt"

CFG_LOG_BASE_FMT = "[%(asctime)s] [%(levelname)s] %(message)s"
CFG_LOG_DATE_FMT = "%H:%M/%d.%m.%y"

# CFG

class CFGException(Exception):
    pass

# cfg_wl

def cfg_wl_src() -> list[int]:
    global CFG_WL_SRC
    if "CFG_WL_SRC" in globals():
        return CFG_WL_SRC
    with open(file = CFG_WL_PATH, mode = CFG_WL_MODE, encoding = CFG_WL_ENCODING) as wl:
        if not wl.readable():
            raise CFGException()
        CFG_WL_SRC = [int(wlr.strip()) for wlr in wl.readlines()]
        return CFG_WL_SRC

# cfg_tg

def cfg_tg_tkn_src() -> str:
    global CFG_TG_TKN_SRC
    if "CFG_TG_TKN_SRC" in globals():
        return CFG_TG_TKN_SRC
    with open(file = CFG_TG_TKN_PATH, mode = CFG_TG_TKN_MODE, encoding = CFG_TG_TKN_ENCODING) as tkn:
        if not tkn.readable():
            raise CFGException()
        CFG_TG_TKN_SRC = "".join(tkn.readlines()).strip()
        return CFG_TG_TKN_SRC

# cfg_kp

def cfg_kp_tkn_src() -> str:
    global CFG_KP_TKN_SRC
    if "CFG_KP_TKN_SRC" in globals():
        return CFG_KP_TKN_SRC
    with open(file = CFG_KP_TKN_PATH, mode = CFG_KP_TKN_MODE, encoding = CFG_KP_TKN_ENCODING) as tkn:
        if not tkn.readable():
            raise CFGException()
        CFG_KP_TKN_SRC = "".join(tkn.readlines()).strip()
        return CFG_KP_TKN_SRC

# cfg_log

def cfg_log_lvl() -> int:
    global CFG_LOG_LVL
    if "CFG_LOG_LVL" in globals():
        return CFG_LOG_LVL
    CFG_LOG_LVL = CFG_LOG_IN_DEVELOPMENT_LVL if CFG_BOT_IN_DEVELOPMENT else CFG_LOG_PRODUCTION_LVL
    return CFG_LOG_LVL
