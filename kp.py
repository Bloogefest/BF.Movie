#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from kinopoisk_dev import *

from cfg import cfg_kp_tkn_src

KP_INSTANCE: KinopoiskDev

def kp_get_instance() -> KinopoiskDev:
    global KP_INSTANCE
    if "KP_INSTANCE" in globals():
        return KP_INSTANCE
    KP_INSTANCE = KinopoiskDev(cfg_kp_tkn_src())
    return KP_INSTANCE
