import sys
import json
import os.path


default_config = {
    "labels": {
        "Orbital Elements": "Orbital Elements",
        "Orbital Nodes": "Orbital Nodes"
    },
    "preview_interval": 10,
    "sliders": {
        "e": 0.5,
        "i": 40,
        "o": 10,
        "w": 270,
        "v": 0
    }
}


def create_config(config_path):
    with open(config_path, 'w') as conf_file:
        json.dump(default_config, conf_file, indent=2)


def parse_config():
    if getattr(sys, 'frozen', False): # If the programm is running as a packaged application, use the global config file
        config_path = os.path.expanduser('~') + '/.config/astrometor/config.json'
    else: # Otherwise use the local config file
        config_path = 'config.json' # Change this value if you want a different configuration path

    if not os.path.exists(config_path):
        create_config(config_path)

    with open(config_path, 'r') as conf_file:
        try:
            config = json.load(conf_file)
        except:
            print("There's a json formatting error in your config.json file. Using the default configuration.")
            return default_config

        if not validate_config(config):
            print("Your config file contains an error.")
            print("For information on correct configuration please read the Configuration section in the readme:")
            print("https://github.com/koslowto/astrometor?tab=readme-ov-file#configuration")
            return default_config

    return config


def validate_config(config):
    valid_config = default_config

    if config.keys() != valid_config.keys():
        return False

    if len(config["labels"]) != 2:
        return False
    for key in config["labels"]:
        if not (config["labels"][key] in ["Orbital Elements", "Orbital Nodes"]):
            return False

    if not isinstance(config["preview_interval"], (int, float)):
        return False

    if config["sliders"].keys() != valid_config["sliders"].keys():
        return False
    for key in config["sliders"]:
        if not isinstance(config["sliders"][key], (int, float)):
            return False

    return True
