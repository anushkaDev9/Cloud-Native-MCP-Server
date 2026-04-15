# Records all requests, responses, and errors for auditing and monitoring
# Handles audit logging for tool requests and responses

# Handles audit logging for tool requests and responses

import logging
from datetime import datetime

logging.basicConfig(
    filename="mcp_logs.log",
    level=logging.INFO,
    format="%(message)s"
)

def log_event(user_id, role, tool_name, status, details=""):
    log_data = {
        "timestamp": datetime.utcnow().isoformat(),
        "user_id": user_id,
        "role": role,
        "tool": tool_name,
        "status": status,
        "details": details
    }

    logging.info(log_data)


def log_error(user_id, role, tool_name, error):
    log_data = {
        "timestamp": datetime.utcnow().isoformat(),
        "user_id": user_id,
        "role": role,
        "tool": tool_name,
        "status": "error",
        "error": str(error)
    }

    logging.error(log_data)