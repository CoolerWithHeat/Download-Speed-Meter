import os

def load_env_vars(keys, filepath=".env"):
    try:
        with open(filepath, "r") as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue

                key, value = line.split("=", 1)
                key = key.strip()

                if key in keys:
                    value = value.strip().strip('"').strip("'")
                    os.environ.setdefault(key, value)

    except FileNotFoundError:
        pass

load_env_vars([
    "request_frequency",
])