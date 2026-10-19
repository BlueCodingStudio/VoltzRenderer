import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SETTINGS = os.path.join(SCRIPT_DIR, "settings.json")
OUTPUT = SCRIPT_DIR + "\output"

def load():
    global data
    try:
        with open(SETTINGS, "r") as f:
            data = json.load(f)
            return(data)
    except FileNotFoundError:
        with open(SETTINGS, "w") as f:
            items = ["empty", f"{OUTPUT}"]
            f.write((str(items)).replace("'", '"'))
        with open(SETTINGS, "r") as f:
            data = json.load(f)
            return(data)

def save(blenderexec, outputfile):
    with open(SETTINGS, "w") as f:
        items = [blenderexec, outputfile]
        json.dump(items, f)


def reset():
    with open(SETTINGS, "w") as f:
        items = ["empty", OUTPUT]
        json.dump(items, f)
