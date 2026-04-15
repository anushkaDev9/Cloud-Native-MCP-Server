# Manages storage and retrieval of available tools and their metadata
# Manages available tools and their metadata for lookup and validation

TOOLS = [
    {
        "tool_name": "s3_list_files",
        "description": "Lists files from an S3 bucket",
        "required_params": ["bucket_name"],
        "allowed_roles": ["admin", "viewer", "devops"]
    },
    {
        "tool_name": "s3_list_buckets",
        "description": "Lists all S3 buckets",
        "allowed_roles": ["admin", "user", "viewer", "developer"],
        "required_params": []
    },
    {
        "tool_name": "ec2_start_instance",
        "description": "Starts an EC2 instance",
        "required_params": ["instance_id"],
        "allowed_roles": ["admin", "devops"]
    },
    {
        "tool_name": "github_create_issue",
        "description": "Creates a new GitHub issue in a repository",
        "required_params": ["repo", "title", "body"],
        "allowed_roles": ["admin", "developer"]
    }
]


def get_all_tools():
    return TOOLS


def get_tool_by_name(tool_name: str):
    for tool in TOOLS:
        if tool["tool_name"] == tool_name:
            return tool
    return None