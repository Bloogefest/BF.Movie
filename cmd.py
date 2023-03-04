#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from typing import *

from str import *

def cmd_build_schema_element(schema: dict[str, Any],
                             built_schema: dict[str, function] = None,
                             path: str = "") -> dict[str, function]:
    for key in schema:
        value = schema[key]
        if type(value) is dict:
            cmd_build_schema_element(value, built_schema, path + STR_CMD_ELEMENT_SEPARATOR + key)
        else:
            built_schema[path + STR_CMD_ELEMENT_SEPARATOR + key] = value
    return built_schema

def cmd_build_schema(schema: dict[str, Any]) -> dict[str, function]:
    return cmd_build_schema_element(schema)

CMD_INSTANCE_SCHEMA = cmd_build_schema(STR_CMD_SCHEMA)
