# 📦 File Monitor with Celery & Docker

A lightweight Python service using **Celery** to monitor a file. If the file is not empty, its content is securely moved to another folder and the original file is cleared.

---

## 🚀 Features

- 📄 Monitors a target file continuously
- 🔍 Checks if the file is empty or not
- ✂️ Moves content to a secure directory if data exists
- 🔁 Runs asynchronously using Celery workers
- 🐳 Fully containerized with Docker
- ⚡ Easy to deploy and scale

---

## 🏗️ Project Structure

```
.
├── app/
│   ├── tasks.py
│   ├── worker.py
│   └── config.py
├── data/
│   ├── input.txt
│   └── secure/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

1. A Celery worker runs periodically.
2. It checks `input.txt`.
3. If the file is not empty:
   - Content is copied to the `secure/` folder
   - Original file is cleared

---

## 🐳 Docker Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/file-monitor-celery.git
cd file-monitor-celery
```

### 2. Build and run containers

```
docker-compose up --build
```

---

## 🧠 Requirements

- Docker
- Docker Compose

---

## 📦 Services

- Celery Worker
- Redis

---

## 🔧 Configuration

Edit `app/config.py`:

```python
FILE_PATH = "/app/data/input.txt"
SECURE_FOLDER = "/app/data/secure/"
CHECK_INTERVAL = 10
```

---

## 🧪 Example Celery Task

```python
from celery import shared_task
import os
from datetime import datetime

FILE_PATH = "/app/data/input.txt"
SECURE_FOLDER = "/app/data/secure/"

@shared_task
def check_file():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r+") as f:
            content = f.read().strip()
            if content:
                filename = f"{SECURE_FOLDER}/backup_{datetime.now().timestamp()}.txt"
                with open(filename, "w") as secure_file:
                    secure_file.write(content)

                f.truncate(0)
```

---

## 🔁 Scheduling Tasks

Example using Celery Beat:

```python
app.conf.beat_schedule = {
    'check-file-every-10-seconds': {
        'task': 'app.tasks.check_file',
        'schedule': 10.0,
    },
}
```

---

## 🛡️ Security Notes

- Ensure the `secure/` folder has restricted permissions
- Avoid exposing sensitive data via logs
- Use environment variables for production configs

---

## 📈 Future Improvements

- Add file encryption before storage
- Support multiple files monitoring
- Add logging and alert system
- Web dashboard for monitoring

---

## 🤝 Contributing

Pull requests are welcome!

---

## 📄 License

MIT License
