import os
from dotenv import load_dotenv
from google.genai import types
from google import genai
import sys
import argparse
load_dotenv()
#________________________________________________________________#
parser = argparse.ArgumentParser()

parser.add_argument(sys.argv[1],type=str, help="Input string")
parser.add_argument('-v', '--verbose',
                    action='store_true')  # on/off flag # 

args = parser.parse_args()
verbose = args.verbose
#________________________________________________________________#

messages = [
    types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),
]

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


if sys.argv[1]:
    response = client.models.generate_content(
    model='gemini-2.5-flash', contents=messages
    )
    print(response.text)
    if verbose:
        if response.usage_metadata:
            print(f"User prompt: {sys.argv[1]}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
            #print(f"Total Token Count: {response.usage_metadata.total_token_count}")
        else:
            print("Usage metadata not available in this response.")
else:
    Exception("No input provided")
    sys.exit(1)
