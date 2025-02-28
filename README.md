# Service Monitoring API

## 📌 Description
Service Monitoring API is a system that monitors web/API services, sends alerts when a service goes offline, and generates uptime/downtime statistics.

## 🚀 Technologies Used
- **Python** 3.13
- **FastAPI** (REST API)
- **Celery** (Asynchronous Tasks)
- **Redis** (Task Queue)
- **SQLite** (Database)
- **Docker & Docker Compose** (Containerization)
- **Telegram API** (Alert Notifications)

---

## 📂 Project Structure

```
service_monitoring/
│── app/
│   ├── api/
│   │   ├── endpoints/
│   │   │   ├── services.py
│   │   │   ├── alerts.py
│   │   │   ├── users.py
│   │   │   ├── __init__.py
│   │   ├── __init__.py
│   │   ├── dependencies.py
│   ├── core/
│   │   ├── celery_worker.py
│   │   ├── celery_config.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── logging_config.py
│   │   ├── __init__.py
│   ├── models/
│   │   ├── service.py
│   │   ├── alert.py
│   │   ├── __init__.py
│   ├── schemas/
│   │   ├── service.py
│   │   ├── alert.py
│   │   ├── __init__.py
│   ├── services/
│   │   ├── alert_manager.py
│   │   ├── service_monitor.py
│   │   ├── telegram_bot.py
│   │   ├── __init__.py
│   ├── tests/
│   ├── main.py
│── docker-compose.yml
│── Dockerfile
│── .env
│── requirements.txt
│── README.txt
```

---

## 🔹 Installation and Configuration

### 1️⃣ Clone the repository
```bash
git clone https://github.com/CarlosOliveira-23/service-monitoring.git
cd service-monitoring
```

### 2️⃣ Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts ctivate  # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set up environment variables
Create a `.env` file and add:
```
TELEGRAM_BOT_TOKEN=your_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
DATABASE_URL=sqlite:///./service_monitoring.db
REDIS_URL=redis://localhost:6379/0
```

---

## 🏃‍♂️ Running the Application

### **Running Locally**
1. Start FastAPI:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
Access the API documentation at `http://127.0.0.1:8000/docs`.

2. Start Redis (if not running):
```bash
docker run -d -p 6379:6379 redis
```

3. Start Celery Worker:
```bash
celery -A app.core.celery_worker worker --loglevel=info
```

4. Start Celery Beat (task scheduler):
```bash
celery -A app.core.celery_worker beat --loglevel=info
```

---

## 🐳 Running with Docker
1. **Build the containers**
```bash
docker-compose build
```

2. **Start the services**
```bash
docker-compose up
```
Access the API at `http://localhost:8000`.

---

## 🧪 Testing the Application

1. **Run tests**
```bash
pytest tests/
```

2. **Manually test the API**
- Create a service:
```bash
curl -X 'POST' 'http://127.0.0.1:8000/services/' -H 'Content-Type: application/json' -d '{
  "name": "Google",
  "url": "https://www.google.com"
}'
```

- List services:
```bash
curl -X 'GET' 'http://127.0.0.1:8000/services/'
```

- Delete a service:
```bash
curl -X 'DELETE' 'http://127.0.0.1:8000/services/1'
```

---

## 📬 Sending Alerts to Telegram
- The bot sends messages when a service goes offline.
- To manually test:
```python
from app.services.telegram_bot import send_telegram_alert
send_telegram_alert("🚨 Test Alert! 🚨")
```

If everything is set up correctly, you should receive the message on Telegram. 🚀

---

## 📌 Next Steps
- Improve automated tests 🧪
- Create a React dashboard 📊
- Deploy the application to the cloud ☁️

---

✅ **100% Open Source Project!** Contributions are welcome! 🎉
