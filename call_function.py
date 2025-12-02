from google.genai import types
import inspect
from functions.get_files_info import schema_get_files_info,get_files_info
from functions.get_file_content import schema_get_file_content,get_file_content
from functions.run_python_file import schema_run_python_file,run_python_file
from functions.write_file import schema_write_file,write_file


available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file
    ]
)

function_map = {
     'get_files_info' : get_files_info,
     'get_file_content' : get_file_content,
     'run_python_file' : run_python_file,
     'write_file' : write_file,
}

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
            print(f" - Calling function: {function_call_part.name}")
        
    try:
        function_name = function_call_part.name
        args = {**function_call_part.args,"working_directory" : "./calculator"}
        
        sig = inspect.signature(function_map[function_name])
        param_names = list(sig.parameters.keys())
        filtered_args = {k: v for k, v in args.items() if k in param_names}


        function_result = function_map[function_name](**filtered_args)
        return types.Content(
        role="tool",
        parts=[
        types.Part.from_function_response(
            name=function_name,
            response={"result": function_result},
        )
    ],
)
    except KeyError:
        return types.Content(
        role="tool",
        parts=[
        types.Part.from_function_response(
            name=function_name,
            response={"error": f"Keyerror Unknown function: {function_name}"},
        )
        ],
)
    except TypeError:
        return types.Content(
        role="tool",
        parts=[
        types.Part.from_function_response(
            name=function_name,
            response={"error": f"the arguments don't match the function signature function: {function_name}"},
        )
        ],
)
    except:
        return types.Content(
        role="tool",
        parts=[
        types.Part.from_function_response(
            name=function_name,
            response={"error": f"Unknown function: {function_name}"},
        )
        ],
)
