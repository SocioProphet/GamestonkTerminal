import json

from openbb_terminal.core.config.paths import USER_DATA_SOURCES_DEFAULT_FILE


def test_sources_load():
    with open(str(USER_DATA_SOURCES_DEFAULT_FILE)) as json_file:
        json_doc = json.load(json_file)
    assert isinstance(json_doc, dict)
    assert "stocks" in json_doc
