from app.services.tool_registry import get_tool_by_name
from app.services.logger_service import log_event, log_error
from app.tools.s3_tool import list_s3_files, list_s3_buckets
from app.tools.ec2_tool import start_ec2_instance
from app.tools.github_tool import create_github_issue


def execute_tool(request, user):
    tool = get_tool_by_name(request.tool_name)

    if not tool:
        log_error(
            user_id=user["user_id"],
            role=user["role"],
            tool_name=request.tool_name,
            error="Tool not found"
        )
        return {
            "status": "error",
            "tool_name": request.tool_name,
            "result": "Tool not found"
        }, 404

    if user["role"] not in tool["allowed_roles"]:
        log_error(
            user_id=user["user_id"],
            role=user["role"],
            tool_name=request.tool_name,
            error=f"Access denied. Params: {request.parameters}"
        )
        return {
            "status": "error",
            "tool_name": request.tool_name,
            "result": f"Access denied for role: {user['role']}"
        }, 403

    missing_params = [
        param for param in tool["required_params"]
        if param not in request.parameters
    ]

    if missing_params:
        log_error(
            user_id=user["user_id"],
            role=user["role"],
            tool_name=request.tool_name,
            error=f"Missing params: {missing_params}"
        )
        return {
            "status": "error",
            "tool_name": request.tool_name,
            "result": f"Missing required parameters: {missing_params}"
        }, 400

    try:
        # 🔹 Start log
        log_event(
            user_id=user["user_id"],
            role=user["role"],
            tool_name=request.tool_name,
            status="started",
            details=str(request.parameters)
        )

        result = run_tool(request.tool_name, request.parameters)

        # 🔹 Success log
        log_event(
            user_id=user["user_id"],
            role=user["role"],
            tool_name=request.tool_name,
            status="success",
            details=str(result)
        )

        return {
            "status": "success",
            "tool_name": request.tool_name,
            "result": result
        }, 200

    except Exception as e:
        # 🔹 Error log
        log_error(
            user_id=user["user_id"],
            role=user["role"],
            tool_name=request.tool_name,
            error=str(e)
        )
        return {
            "status": "error",
            "tool_name": request.tool_name,
            "result": str(e)
        }, 500


def run_tool(tool_name, params):
    if tool_name == "s3_list_files":
        return list_s3_files(params["bucket_name"])

    elif tool_name == "s3_list_buckets":
        return list_s3_buckets()

    elif tool_name == "ec2_start_instance":
        return start_ec2_instance(params["instance_id"])

    elif tool_name == "github_create_issue":
        return create_github_issue(
            repo=params["repo"],
            title=params["title"],
            body=params["body"]
        )

    raise Exception("Unsupported tool")