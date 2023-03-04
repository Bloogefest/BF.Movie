#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from enum import Enum
from typing import Optional

from kinopoisk_dev import *
from kinopoisk_dev import MovieParams

from cfg import cfg_kp_tkn_src

KP_INSTANCE: KinopoiskDev

class KPFilter:

    def to_kp_api(self) -> list[MovieParams]:
        pass

class KPMovieType(Enum):
    MOVIE = "movie"
    TV_SERIES = "tv-series"
    CARTOON = "cartoon"
    ANIME = "anime"
    ANIMATED_SERIES = "animated_series"
    TV_SHOW = "tv-show"

class KPTypeFilter(KPFilter):

    def __init__(self, types: list[KPMovieType] = None) -> None:
        self.types = list() if types is None else types

    def to_kp_api(self) -> list[MovieParams]:
        return [MovieParams(Field.TYPE, type_.name) for type_ in self.types]

    def add_type(self, type_: KPMovieType) -> None:
        if type_ not in self.types:
            self.types.append(type_)

    def remove_type(self, type_: KPMovieType) -> None:
        if type_ in self.types:
            self.types.remove(type_)

    def handle_type(self, type_: KPMovieType) -> None:
        if type_ in self.types:
            self.types.remove(type_)
        else:
            self.types.append(type_)

    def clear(self) -> None:
        self.types.clear()

    def check_exists_type(self, type_: KPMovieType) -> bool:
        return type_ in self.types

def kp_get_instance() -> KinopoiskDev:
    global KP_INSTANCE
    if "KP_INSTANCE" in globals():
        return KP_INSTANCE
    KP_INSTANCE = KinopoiskDev(cfg_kp_tkn_src())
    return KP_INSTANCE

def kp_filter_to_api(filter_: Optional[KPFilter]) -> Optional[list[MovieParams]]:
    return None if filter_ is None else filter_.to_kp_api()
