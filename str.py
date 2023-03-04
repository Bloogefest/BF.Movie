#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

# STR_LOG

# STR_CMD

STR_CMD_START = "/start"
STR_CMD_HOME = "/home"
STR_CMD_SEARCH = "/search"

STR_CMD_SEARCH_CONFIRM = "/search_confirm"
STR_CMD_SEARCH_FILTERS = "/search_filters"
STR_CMD_SEARCH_FILTERS_RESET = "/search_filters_reset"

STR_CMD_SEARCH_FILTERS_MOVIE_TYPE = "/search_filters_movie-type"
STR_CMD_SEARCH_FILTERS_MOVIE_TYPE_MOVIE = "/search_filters_movie-type_movie"
STR_CMD_SEARCH_FILTERS_MOVIE_TYPE_TV_SERIES = "/search_filters_movie-type_tv-series"
STR_CMD_SEARCH_FILTERS_MOVIE_TYPE_CARTOON = "/search_filters_movie-type_cartoon"
STR_CMD_SEARCH_FILTERS_MOVIE_TYPE_ANIME = "/search_filters_movie-type_anime"
STR_CMD_SEARCH_FILTERS_MOVIE_TYPE_ANIMATED_SERIES = "/search_filters_movie-type_animated-series"
STR_CMD_SEARCH_FILTERS_MOVIE_TYPE_TV_SHOW = "/search_filters_movie-type_tv-show"
STR_CMD_SEARCH_FILTERS_MOVIE_TYPE_RESET = "/search_filters_movie-type_reset"

STR_CMD_SEARCH_FILTERS_MOVIE_STATUS = "/search_filters_movie-status"
STR_CMD_SEARCH_FILTERS_MOVIE_STATUS_FILMING = "/search_filters_movie-status_filming"
STR_CMD_SEARCH_FILTERS_MOVIE_STATUS_PRE_PRODUCTION = "/search_filters_movie-status_pre-production"
STR_CMD_SEARCH_FILTERS_MOVIE_STATUS_COMPLETED = "/search_filters_movie-status_completed"
STR_CMD_SEARCH_FILTERS_MOVIE_STATUS_ANNOUNCED = "/search_filters_movie-status_announced"
STR_CMD_SEARCH_FILTERS_MOVIE_STATUS_POST_PRODUCTION = "/search_filters_movie-status_post-production"
STR_CMD_SEARCH_FILTERS_MOVIE_STATUS_RESET = "/search_filters_movie-status_reset"

STR_CMD_HELP = "/help"

STR_CMD_ABOUT = "/about"

# STR_MENU

STR_MENU_HOME_BTN_SEARCH = "Поиск"
STR_MENU_HOME_BTN_HELP = "Справка"
STR_MENU_HOME_BTN_ABOUT = "О боте"

STR_MENU_SEARCH_BTN_HOME = "В главное меню"
STR_MENU_SEARCH_BTN_CONFIRM = "Подтвердить"
STR_MENU_SEARCH_BTN_FILTERS = "Фильтры"

STR_MENU_SEARCH_RESULTS_BTN_NEXT = "Следующий"
STR_MENU_SEARCH_RESULTS_BTN_PREVIOUS = "Предыдущий"
STR_MENU_SEARCH_RESULTS_BTN_PARENT = "К поиску"

STR_MENU_SEARCH_FILTERS_BTN_MOVIE_TYPE = "По типу"
STR_MENU_SEARCH_FILTERS_BTN_MOVIE_STATUS = "По статусу"
STR_MENU_SEARCH_FILTERS_BTN_PARENT = "К поиску"
STR_MENU_SEARCH_FILTERS_BTN_RESET = "Сбросить"

STR_MENU_SEARCH_FILTERS_MOVIE_TYPE_BTN_MOVIE = "Фильм"
STR_MENU_SEARCH_FILTERS_MOVIE_TYPE_BTN_TV_SERIES = "Телесериал"
STR_MENU_SEARCH_FILTERS_MOVIE_TYPE_BTN_CARTOON = "Мультфильм"
STR_MENU_SEARCH_FILTERS_MOVIE_TYPE_BTN_ANIME = "Аниме"
STR_MENU_SEARCH_FILTERS_MOVIE_TYPE_BTN_ANIMATED_SERIES = "Анимационный сериал"
STR_MENU_SEARCH_FILTERS_MOVIE_TYPE_BTN_TV_SHOW = "Телешоу"
STR_MENU_SEARCH_FILTERS_MOVIE_TYPE_BTN_PARENT = "К фильтрам"
STR_MENU_SEARCH_FILTERS_MOVIE_TYPE_BTN_RESET = "Сбросить"

STR_MENU_SEARCH_FILTERS_MOVIE_STATUS_BTN_FILMING = "Снимается"
STR_MENU_SEARCH_FILTERS_MOVIE_STATUS_BTN_PRE_PRODUCTION = "На предпроизводственном этапе"
STR_MENU_SEARCH_FILTERS_MOVIE_STATUS_BTN_COMPLETED = "Завершён"
STR_MENU_SEARCH_FILTERS_MOVIE_STATUS_BTN_ANNOUNCED = "Анонсирован"
STR_MENU_SEARCH_FILTERS_MOVIE_STATUS_BTN_POST_PRODUCTION = "На послепроизводственном этапе"
STR_MENU_SEARCH_FILTERS_MOVIE_STATUS_BTN_PARENT = "К фильтрам"
STR_MENU_SEARCH_FILTERS_MOVIE_STATUS_BTN_RESET = "Сбросить"

STR_MENU_HELP_BTN_HOME = "В главное меню"

STR_MENU_ABOUT_BTN_HOME = "В главное меню"

# STR_MSG

STR_MSG_ABOUT_STATUS_IN_PRODUCTION = "В продакшене"
STR_MSG_ABOUT_STATUS_IN_DEVELOPMENT = "В разработке"

STR_MSG_SEARCH_FILTERS_MOVIE_TYPE_NOT_SELECTED = "\nНичего"
STR_MSG_SEARCH_FILTERS_MOVIE_TYPE_SELECTED_PREFIX = "\n- "

STR_MSG_SEARCH_FILTERS_MOVIE_STATUS_NOT_SELECTED = "\nНичего"
STR_MSG_SEARCH_FILTERS_MOVIE_STATUS_SELECTED_PREFIX = "\n- "

# STR_CMD

STR_CMD_SCHEMA = {
    "/": {
        "start": lambda msg: None,
        "home": lambda msg: None,
        "search": {
            "results": {
                "previous": lambda msg: None,
                "open": lambda msg: None,
                "next": lambda msg: None
            },
            "confirm": lambda msg: None,
            "filters": {
                "type": {
                    "movie": lambda msg: None,
                    "tv-series": lambda msg: None,
                    "cartoon": lambda msg: None,
                    "anime": lambda msg: None,
                    "animated-series": lambda msg: None,
                    "tv-show": lambda msg: None,
                    "reset": lambda msg: None
                },
                "status": {
                    "filming": lambda msg: None,
                    "pre-production": lambda msg: None,
                    "completed": lambda msg: None,
                    "announced": lambda msg: None,
                    "post-production": lambda msg: None,
                    "reset": lambda msg: None
                },
                "reset": lambda msg: None
            }
        },
        "help": {},
        "about": {}
    }
}

STR_CMD_ELEMENT_SEPARATOR = " "

# STR_MENU

STR_MENU_SCHEMA_HOME = {
    "Поиск": lambda msg: None,
    {
        "Справка": lambda msg: None,
        "О боте": lambda msg: None
    }: None
}

STR_MENU_SCHEMA_SEARCH = {
    "Искать": lambda msg: None,
    {
        "В главное меню": lambda msg: None,
        "Фильтры": lambda msg: None
    }: None
}

STR_MENU_SCHEMA_SEARCH_RESULTS = {
    "Предыдущий": lambda msg: None,
    "Открыть в Кинопоиске": lambda msg: None,
    "Следующий": lambda msg: None
}

STR_MENU_SCHEMA_SEARCH_FILTERS = {
    {
        "По типу": lambda msg: None,
        "По статусу": lambda msg: None
    }: None,
    {
        "К поиску": lambda msg: None,
        "Сбросить": lambda msg: None
    }: None
}

STR_MENU_SCHEMA_SEARCH_FILTERS_TYPE = {
    {
        "Фильм": lambda msg: None,
        "Телесериал": lambda msg: None
    }: None,
    {
        "Мультфильм": lambda msg: None,
        "Аниме": lambda msg: None
    }: None,
    {
        "Анимационный сериал": lambda msg: None,
        "Телешоу": lambda msg: None
    }: None,
    {
        "К фильтрам": lambda msg: None,
        "Сбросить": lambda msg: None
    }: None
}

STR_MENU_SCHEMA_SEARCH_FILTERS_STATUS = {
    {
        "Анонсирован": lambda msg: None,
        "Снимается": lambda msg: None
    }: None,
    "На предпроизводственном этапе": lambda msg: None,
    "На послепроизводственном этапе": lambda msg: None,
    "Завершён": lambda msg: None,
    {
        "К фильтрам": lambda msg: None,
        "Сбросить": lambda msg: None
    }: None
}

STR_MENU_SCHEMA_HELP = {
    "В главное меню": lambda msg: None
}

STR_MENU_SCHEMA_ABOUT = {
    "В главное меню": lambda msg: None
}
