#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from cfg import CFG_BOT_VERSION, CFG_BOT_IN_DEVELOPMENT
from session import Session
from str import *

MSG_CMD_START = """\
Выберите действие.
"""

MSG_CMD_HOME = """\
Выберите действие.
"""

MSG_CMD_SEARCH = """\
Поиск временно недоступен.
"""

MSG_CMD_SEARCH_CONFIRM = """\
Подтверждение временно недоступно.
"""

MSG_CMD_SEARCH_FILTERS = """\
Выберите действие.
"""

MSG_CMD_SEARCH_FILTERS_RESET = """\
Фильтры успешно сброшены.
"""

MSG_CMD_SEARCH_FILTERS_MOVIE_TYPE = """\
Выберите тип.
Выбрано:
"""

MSG_CMD_SEARCH_FILTERS_MOVIE_STATUS = """\
Выберите статус.
Выбрано:
"""

MSG_CMD_HELP = """\
Справка временно недоступна.
"""

MSG_CMD_ABOUT = f"""\
Текущая версия: {CFG_BOT_VERSION}
Статус: {STR_MSG_ABOUT_STATUS_IN_DEVELOPMENT if CFG_BOT_IN_DEVELOPMENT else STR_MSG_ABOUT_STATUS_IN_PRODUCTION}
"""

def msg_get_cmd_search_filters_movie_type(session: Session) -> str:
    msg = MSG_CMD_SEARCH_FILTERS_MOVIE_TYPE
    any_exists = False
    if len(session.search_filter_movie_type.types) > 0:
        msg += "".join([STR_MSG_SEARCH_FILTERS_MOVIE_TYPE_SELECTED_PREFIX + type_.name for type_ in session.search_filter_movie_type.types])
    if not any_exists:
        msg += STR_MSG_SEARCH_FILTERS_MOVIE_TYPE_NOT_SELECTED
        return msg

def msg_get_cmd_search_filters_movie_status(session: Session) -> str:
    msg = MSG_CMD_SEARCH_FILTERS_MOVIE_STATUS
    any_exists = False
    if len(session.search_filter_movie_status.statuses) > 0:
        msg += "".join([STR_MSG_SEARCH_FILTERS_MOVIE_STATUS_SELECTED_PREFIX + status.name for status in session.search_filter_movie_status.statuses])
    if not any_exists:
        msg += STR_MSG_SEARCH_FILTERS_MOVIE_STATUS_NOT_SELECTED
        return msg
