import json
import os.path

# The preset config path only works on Linux. If your on windows comment it, and uncomment the line after.
# This will create an editable config file in the same directory as the python program.
# On Linux you can do the same if you don't want the config file in your .config/ directory.
config_path = os.path.expanduser('~') + '/.config/astrometor/config.json'
#config_path = 'config.json'

default_config = { "labels": {"Orbital Elements": "Orbital Elements", "Orbital Nodes": "Orbital Nodes"},
    "preview_interval": 10, "sliders": {"e": 0.5, "i": 40, "o": 10, "w": 270, "v": 0} }

def parse_config():
    if not os.path.exists(config_path):
        create_config(config_path)

    with open(config_path, 'r') as conf_file:
        try:
            config = json.load(conf_file)
        except:
            print("There's a json formatting error in your config.json file. Using the default configuration.")
            return default_config

        if not validate_config(config):
            print("Your config file contains an error. For information on correct configuration please read the Configuration section in the readme (https://github.com/koslowto/astrometor).")
            return default_config

    return config


def create_config(config_path):
    with open(config_path, 'w') as conf_file:
        json.dump(default_config, conf_file, indent=2)


def validate_config(config):
    valid_config = default_config

    if config.keys() != valid_config.keys():
        return False

    if len(config["labels"]) != 2:
        return False
    for key in config["labels"]:
        if not (config["labels"][key] in ["Orbital Elements", "Orbital Nodes"]):
            return False

    if not isinstance(config["preview_interval"], int):
        return False

    if config["sliders"].keys() != valid_config["sliders"].keys():
        return False
    for key in config["sliders"]:
        if not isinstance(config["sliders"][key], (int, float)):
            return False

    return True
