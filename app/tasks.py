import os
from datetime import datetime
from app.celery_app import celery_app
from app.config import FILE_PATH, SECURE_FOLDER

@celery_app.task
def check_file():
    if not os.path.exists(FILE_PATH):
        return "File does not exist"

    os.makedirs(SECURE_FOLDER, exist_ok=True)

    with open(FILE_PATH, "r+") as f:
        content = f.read().strip()
        if content:
            filename = os.path.join(
                SECURE_FOLDER,
                f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            )

            with open(filename, "w") as secure_file:
                secure_file.write(content)

            f.seek(0)
            f.truncate(0)

            return f"Moved content to {filename}"

    return "File is empty"
