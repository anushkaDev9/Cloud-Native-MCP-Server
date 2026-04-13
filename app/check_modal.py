import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
def main():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Set your GEMINI_API_KEY environment variable first.")

    client = genai.Client(api_key=api_key)

    print("Available Gemini models:\n")
    found = False

    for model in client.models.list():
        name = getattr(model, "name", "")
        display_name = getattr(model, "display_name", "")
        description = getattr(model, "description", "")

        # Show only Gemini models
        if "gemini" in name.lower():
            found = True
            print(f"Model ID      : {name}")
            print(f"Display Name  : {display_name}")
            print(f"Description   : {description}")
            print("-" * 60)

    if not found:
        print("No Gemini models were returned for this API key.")

if __name__ == "__main__":
    main()