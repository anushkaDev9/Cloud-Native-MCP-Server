from fastapi import APIRouter, HTTPException
from app.auth import API_KEYS
from app.models.schemas import (
    ToolInvokeRequest,
    ToolInvokeResponse,
    ToolInfo,
    HealthResponse
)
from app.services.tool_registry import get_all_tools
from app.services.executor import execute_tool
from app.tools.s3_tool import list_s3_buckets

router = APIRouter()


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
    api_key = request.api_key

    # Validate API key
    if api_key not in API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    # Get role from API key
    role = API_KEYS[api_key]

    user = {
        "user_id": api_key,
        "role": role
    }

    response, status_code = execute_tool(request, user)

    if status_code != 200:
        raise HTTPException(status_code=status_code, detail=response["result"])

    return response

