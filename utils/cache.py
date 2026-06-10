import json
import os


CACHE_FILE = "data/cache.json"


def save_cache(data):

    with open(
        CACHE_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )


def load_cache():

    if not os.path.exists(
        CACHE_FILE
    ):
        return None

    try:

        with open(
            CACHE_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

            if not data:
                return None

            return data

    except Exception:

        return None