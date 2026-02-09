import os
from dotenv import load_dotenv
from google import genai
import argparse

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("Environment variable GEMINI_API_KEY not found. Make sure it is set in your .env file.")

client = genai.Client(api_key=api_key)

prompt = args.user_prompt
response = client.models.generate_content(
    model='gemini-2.5-flash', contents=prompt
)

if response.usage_metadata is None:
    raise RuntimeError("Response usage_metadata is None. The API request may have failed.")

print(f"User prompt: {prompt}")
print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
print("Response:")
print(response.text)

def main():
    print("Hello from ai-agent!")


if __name__ == "__main__":
    main()
