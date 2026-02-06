#Settings persistence - save and load user preferences
import os

SETTINGS_FILE = "portfolio_settings.txt"

def save_settings(port, webroot):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(script_dir, SETTINGS_FILE), "w") as f:
        f.write(f"{port}\n{webroot}\n")

def load_settings():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    settings_path = os.path.join(script_dir, SETTINGS_FILE)
    if os.path.isfile(settings_path):
        try:
            lines = open(settings_path).read().splitlines()
            port = int(lines[0]) if len(lines) > 0 else None
            webroot = lines[1] if len(lines) > 1 else None
            return port, webroot
        except:
            return None, None
    return None, None
