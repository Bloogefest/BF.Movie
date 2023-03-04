#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from log import *
from tg import tg_launch, tg_bot_launch

def main_init():
    log_init()

def main_launch():
    main_init()
    try:
        tg_bot_launch()
    except KeyboardInterrupt:
        pass
    except BaseException as e:
        log_get_logger("main").exception(e.__str__())

if __name__ == "__main__":
    main_launch()
