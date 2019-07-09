# rh_config
This is a repo forked from [Rhoana](https://github.com/Rhoana/rh_config)

## Description
A simple configuration system for the Rhoana pipeline.

Basic usage, either maintain a single config file at ~/.rh-config.yaml or
define the location of the config file in the RH_CONFIG_FILENAME.yaml
environment variable. Put configuration for all of your packages and
applications in this file. Access the loaded configuration like this:

    import rh_config    
    my_default_config = dict(foo="bar")
    ...
    foo = rh_config.config.get("foo", my_default_config.get("foo"))

## Installation
```
$ git clone git@github.com:HoraceKem/rh_config.git
$ cd rh_config/
$ pip install -r requirements.txt
$ pip install --editable .
```
**Tips:**
Create a conda environment before testing the package.
