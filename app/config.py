import os

FILE_PATH = os.getenv("FILE_PATH", "/app/data/input.txt")
SECURE_FOLDER = os.getenv("SECURE_FOLDER", "/app/data/secure/")
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", 10))
