#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
from logging.handlers import RotatingFileHandler
from pathlib import Path

from cfg import *

LOG_FORMATTER = Formatter(fmt = CFG_LOG_BASE_FMT, datefmt = CFG_LOG_DATE_FMT)
LOG_LOGGER_STORAGE = dict[str, Logger]()

def log_init():
    if CFG_LOG_SETUP_CONSOLE:
        log_setup_console()

def log_setup_console():
    logger = getLogger()
    handler = StreamHandler()
    handler.setFormatter(LOG_FORMATTER)
    logger.addHandler(handler)

def log_get_logger(name: str) -> Logger:
    if name in LOG_LOGGER_STORAGE:
        return LOG_LOGGER_STORAGE[name]
    logger = getLogger(name)
    logger.setLevel(cfg_log_lvl())
    Path(CFG_LOG_PARENT_PATH).mkdir(parents = True, exist_ok = True)
    handler = RotatingFileHandler(CFG_LOG_PARENT_PATH + CFG_LOG_PATH_PREFIX + name + CFG_LOG_PATH_SUFFIX, mode = CFG_LOG_MODE, encoding = CFG_LOG_ENCODING, maxBytes = CFG_LOG_MAX_BYTES, backupCount = CFG_LOG_BACKUP_COUNT)
    handler.setFormatter(LOG_FORMATTER)
    logger.addHandler(handler)
    LOG_LOGGER_STORAGE[name] = logger
    return logger
