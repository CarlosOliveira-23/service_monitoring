import logging
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "service_monitoring.log")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="a"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
