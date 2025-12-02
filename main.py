import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from prompt import system_prompt
from call_function import available_functions,call_function


def main():

    load_dotenv()
    
    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I fix the calculator?"')
        sys.exit(1)

    
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)
    
    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages,verbose)




def generate_content(client, messages,verbose):
        response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents=messages,
        config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt),
        )
        
        if verbose:
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        
        if not response.usage_metadata:
            raise RuntimeError("Gemini API response appears to be malformed")

        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
        print(f"Response : \n {response.text}")
        
        if not response.function_calls:
            print(response.text)
        
        else:
            for fn in response.function_calls:
                call = call_function(fn)
                if call.parts[0].function_response.response:
                    list_to_use_later = []
                    list_to_use_later.append(call.parts[0])
                else:
                    Exception("Fatal exception")
                if verbose:
                    print(f"-> {call.parts[0].function_response.response}")
        
if __name__ == "__main__":
    main()
