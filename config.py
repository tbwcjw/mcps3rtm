# config handling for mcps3rtm
# tbwcjw - MIT 2025

import yaml
import os

class Config:
    CONFIG_FILE = "config.yml"

    @staticmethod
    def load():
        if not os.path.exists(Config.CONFIG_FILE):
            return {}
        with open(Config.CONFIG_FILE, "r") as f:
            return yaml.safe_load(f) or {}

    @staticmethod
    def save(config):
        with open(Config.CONFIG_FILE, "w") as f:
            yaml.safe_dump(config, f, default_flow_style=False)

    @staticmethod
    def set(key, value):
        print(f"config set {key}: {value}")
        config = Config.load()
        parts = key.split(".")
        d = config
        for p in parts[:-1]:
            d = d.setdefault(p, {})
        d[parts[-1]] = value
        Config.save(config)

    @staticmethod
    def get(key=None):
        config = Config.load()
        if key is None:
            return config
        parts = key.split(".")
        d = config
        for p in parts:
            if p not in d:
                return None
            d = d[p]
        return d