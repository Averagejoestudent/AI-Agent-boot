import os
from dotenv import load_dotenv
from google import genai
import sys
load_dotenv()
#________________________________________________________________#


api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


if sys.argv[1]:
    content = sys.argv[1]
    response = client.models.generate_content(
    model='gemini-2.5-flash', contents=content
    )
    print(response.text)

    if response.usage_metadata:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        #print(f"Total Token Count: {response.usage_metadata.total_token_count}")
    else:
        print("Usage metadata not available in this response.")
else:
    Exception("No input provided")
    sys.exit(1)
