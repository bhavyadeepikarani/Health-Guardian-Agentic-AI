import json


def load_lottie(filepath):
    """
    Load a Lottie animation from a JSON file.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)