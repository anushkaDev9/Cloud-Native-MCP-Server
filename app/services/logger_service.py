# Records all requests, responses, and errors for auditing and monitoring
# Handles audit logging for tool requests and responses

# Handles audit logging for tool requests and responses

import logging
import os
from app.config import LOG_DIR, LOG_FILE

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def log_event(message: str):
    logging.info(message)


def log_error(message: str):
    logging.error(message)