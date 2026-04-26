
import streamlit as st
import requests
import json
from llm_client import interpret_user_input
from auth import USERS, API_KEYS

st.title("MCP + LLM GitHub Issue Creator")

# --- LOGIN SYSTEM ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if not st.session_state.authenticated:
    st.subheader("Login")
    username_input = st.text_input("Username")
    password_input = st.text_input("Password", type="password")
    if st.button("Login"):
        if username_input in USERS and USERS[username_input]["password"] == password_input:
            st.session_state.authenticated = True
            st.session_state.api_key = USERS[username_input]["api_key"]
            st.session_state.username = username_input
            st.success("Logged in successfully")
            st.rerun()
    else:
        st.error("Invalid username or password")
    st.stop()

# Use authenticated API key
api_key = st.session_state.api_key

# Show role in sidebar
api_key = st.session_state.api_key
role = API_KEYS[api_key]

st.sidebar.write(f"User: {st.session_state.username}")
st.sidebar.write(f"Role: {role}")
repo_name = st.text_input("Repository (username/repo)", value="anushkaDev9/mcp-demo")
st.markdown("### AI Assistant (LLM)")
st.write("Type your request in natural language. The LLM will convert it into a GitHub action.")
user_input = st.text_area(
    "Ask the LLM what you want to do",
    placeholder="Example: Create a GitHub issue saying the server is down"
)
if st.button("Run with LLM"):
    try:
        if not api_key or not repo_name or not user_input:
            st.error("Please fill in API key, repository, and LLM request.")
        else:
            llm_output = interpret_user_input(user_input, repo_name)
            st.subheader("LLM Output")
            st.code(llm_output, language="json")
            parsed = json.loads(llm_output)
            payload = {
                "api_key": api_key,
                "tool_name": parsed["tool_name"],
                "parameters": parsed["parameters"]
            }
            response = requests.post(
                 "http://18.222.28.165:8000/invoke-tool",
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
