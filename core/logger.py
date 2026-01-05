import os
from datetime import datetime

class Logger:

    LOG_DIR = "data"
    LOG_FILE = os.path.join(LOG_DIR, "system.log")

    @staticmethod
    def log(message, level="INFO"):
        os.makedirs(Logger.LOG_DIR, exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] [{level}] {message}\n"
        with open(Logger.LOG_FILE, "a") as f:
            f.write(entry)

    @staticmethod
    def info(message):
        Logger.log(message, "INFO")

    @staticmethod
    def warning(message):
        Logger.log(message, "WARNING")

    @staticmethod
    def error(message):
        Logger.log(message, "ERROR")
