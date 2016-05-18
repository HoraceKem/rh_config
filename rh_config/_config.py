'''Configuration loader'''

import os
import yaml

default_config_filename = os.path.expanduser("~/.rh-config.yaml")
config_filename = os.environ.get("RH_CONFIG_FILENAME", default_config_filename)
if os.path.exists(config_filename):
    config = yaml.load(open(config_filename, "r"))
else:
    config = {}
all = [config]