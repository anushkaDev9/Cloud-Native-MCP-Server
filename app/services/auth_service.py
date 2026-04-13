# Handles user authentication and token validation (JWT/Cognito)
# Handles mock authentication and returns user identity and role from a token

# Handles mock authentication and returns user identity and role from a token

from app.config import TOKENS


def authenticate_token(token: str):
    return TOKENS.get(token)