import os
from dotenv import load_dotenv
from google import genai
from sys import argv


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    gemmodel = "gemini-2.0-flash-001"

    prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

    response = client.models.generate_content(model=gemmodel, contents=prompt)

    print(response.text)
    promptTokenCount = response.usage_metadata.prompt_token_count
    candTokenCount = response.usage_metadata.candidates_token_count
    print(f"Prompt tokens: {promptTokenCount}")
    print(f"Response tokens: {candTokenCount}")


main()
