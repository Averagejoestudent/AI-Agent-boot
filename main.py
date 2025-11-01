import os
from dotenv import load_dotenv
from google import genai
load_dotenv()
#________________________________________________________________#


api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

content = "Why is Boot.dev such great place to learn backend development? Use one paragraph maximum."



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