import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Set GEMINI_API_KEY in your environment or .env file.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def interpret_user_input(user_input: str, repo_name: str) -> str:
    prompt = f"""
You are converting a user request into a JSON tool call.

Tool name:
github_create_issue

Repository:
{repo_name}

Return ONLY valid JSON in this exact structure:
{{
  "tool_name": "github_create_issue",
  "parameters": {{
    "repo": "{repo_name}",
    "title": "short issue title",
    "body": "clear issue description"
  }}
}}

User request:
{user_input}
"""

    response = model.generate_content(prompt)
    text = response.text.strip()

    if text.startswith("```json"):
        text = text[len("```json"):].strip()
    elif text.startswith("```"):
        text = text[len("```"):].strip()

    if text.endswith("```"):
        text = text[:-3].strip()

    # Validate that it is proper JSON before returning
    parsed = json.loads(text)

    # Force repo to match frontend input
    parsed["tool_name"] = "github_create_issue"
    parsed["parameters"]["repo"] = repo_name

    return json.dumps(parsed, indent=2)