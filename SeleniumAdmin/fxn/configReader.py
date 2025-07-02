import configparser
import os

def getConfig(section, key):
    config = configparser.ConfigParser()

    # Get current file's directory (fxn/)
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Navigate to config file: fxn/../config/config.properties
    config_path = os.path.join(base_dir, '..', 'config', 'config.properties')

    config.read(config_path)
    return config.get(section, key)