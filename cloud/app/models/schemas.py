# Defines request and response data models using Pydantic for validation

from pydantic import BaseModel
from typing import Dict, Any, Optional


class ToolInvokeRequest(BaseModel):
    user_id: str
    tool_name: str
    parameters: Dict[str, Any]


class ToolInvokeResponse(BaseModel):
    status: str
    tool_name: str
    result: Any


class ToolInfo(BaseModel):
    tool_name: str
    description: str
    required_params: list[str]
    allowed_roles: list[str]


class HealthResponse(BaseModel):
    status: str
    service: str