import json


def load_sample():

    with open(
        "data/sample_facewash.json",
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)