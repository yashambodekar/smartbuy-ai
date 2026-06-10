import json
import re


def extract_json(text):

    text = text.strip()

    text = re.sub(
        r"^```json",
        "",
        text
    )

    text = re.sub(
        r"^```",
        "",
        text
    )

    text = re.sub(
        r"```$",
        "",
        text
    )

    text = text.strip()

    return json.loads(text)