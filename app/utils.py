import json


def load_messages(path: str):
    with open(path, "r") as f:
        return json.load(f)
