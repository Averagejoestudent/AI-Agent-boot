import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
import argparse
from functions.get_files_info import schema_get_files_info
load_dotenv()
#________________________________________________________________#
parser = argparse.ArgumentParser()

parser.add_argument(sys.argv[1],type=str, help="Input string")
parser.add_argument('-v', '--verbose',
                    action='store_true')  # on/off flag # 

args = parser.parse_args()
verbose = args.verbose
#________________________________________________________________#


system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""


#________________________________________________________________#
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)
messages = [
    types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),
]


api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


if sys.argv[1]:
    response = client.models.generate_content(
    model='gemini-2.5-flash', 
    contents=messages,
    config=types.GenerateContentConfig(
    tools=[available_functions], system_instruction=system_prompt),
    )
    if response.function_calls:
        for fn in response.function_calls:
            print(f"Calling function: {fn.name}({fn.args})")
    else:
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
