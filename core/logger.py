import os
import datetime

class Logger:

    # Detect project root (one level above "core")
    ROOT = os.path.dirname(os.path.dirname(__file__))

    LOG_DIR = os.path.join(ROOT, "data")
    LOG_FILE = os.path.join(LOG_DIR, "system.log")

    @staticmethod
    def log(message):
        # Make sure data/ exists
        os.makedirs(Logger.LOG_DIR, exist_ok=True)

        ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(Logger.LOG_FILE, "a") as f:
            f.write(f"[{ts}] {message}\n")
