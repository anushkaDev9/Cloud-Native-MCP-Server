from fastapi import APIRouter, HTTPException
from app.models.schemas import (
    ToolInvokeRequest,
    ToolInvokeResponse,
    ToolInfo,
    HealthResponse
)
from app.services.tool_registry import get_all_tools
from app.services.executor import execute_tool

router = APIRouter()

# Simple allowlist for demo
ALLOWED_GITHUB_USERS = ["anushkaDev9"]


@router.get("/health", response_model=HealthResponse)
def health_check():
    return {
        "status": "ok",
        "service": "Cloud-Native MCP Server"
    }


@router.get("/tools", response_model=list[ToolInfo])
def list_tools():
    return get_all_tools()


@router.post("/invoke-tool", response_model=ToolInvokeResponse)
def invoke_tool(request: ToolInvokeRequest):
    # If username is in allowlist, give developer role
    if request.user_id in ALLOWED_GITHUB_USERS:
        role = "developer"
    else:
        role = "viewer"

    user = {
        "user_id": request.user_id,
        "role": role
    }

    response, status_code = execute_tool(request, user)

    if status_code != 200:
        raise HTTPException(status_code=status_code, detail=response["result"])

    return response