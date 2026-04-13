# Stores configuration settings like AWS credentials, environment variables, and constants# Lists all Python dependencies required to run the project

# Stores application-wide configuration values and constants

APP_TITLE = "Cloud-Native MCP Server"
APP_DESCRIPTION = "A secure MCP server for enterprise tool integration"
APP_VERSION = "1.0.0"
SERVICE_NAME = "Cloud-Native MCP Server"

LOG_DIR = "logs"
LOG_FILE = f"{LOG_DIR}/audit.log"

TOKENS = {
    "admin-token": {
        "user_id": "admin_user",
        "role": "admin"
    },
    "viewer-token": {
        "user_id": "viewer_user",
        "role": "viewer"
    },
    "devops-token": {
        "user_id": "devops_user",
        "role": "devops"
    },
    "developer-token": {
        "user_id": "developer_user",
        "role": "developer"
    }
}