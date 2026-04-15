import streamlit as st
import requests
import json
from llm_client import interpret_user_input

st.title("MCP + LLM GitHub Issue Creator")

user_id = st.text_input("GitHub Username")
repo_name = st.text_input("Repository (username/repo)", value="anushkaDev9/mcp-demo")

st.markdown("### AI Assistant (LLM)")
st.write("Type your request in natural language. The LLM will convert it into a GitHub action.")

user_input = st.text_area(
    "Ask the LLM what you want to do",
    placeholder="Example: Create a GitHub issue saying the server is down"
)

if st.button("Run with LLM"):
    try:
        if not user_id or not repo_name or not user_input:
            st.error("Please fill in GitHub username, repository, and LLM request.")
        else:
            llm_output = interpret_user_input(user_input, repo_name)

            st.subheader("LLM Output")
            st.code(llm_output, language="json")

            parsed = json.loads(llm_output)

            payload = {
                "user_id": user_id,
                "tool_name": parsed["tool_name"],
                "parameters": parsed["parameters"]
            }

            response = requests.post(
                "http://127.0.0.1:8000/invoke-tool",
                json=payload
            )

            if response.status_code == 200:
                st.success("Issue created!")
                st.json(response.json())
            else:
                st.error("Error")
                st.json(response.json())

    except Exception as e:
        st.error(f"Failed: {e}")