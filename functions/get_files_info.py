import os
import sys
from google.genai import types
def get_files_info(working_directory, directory="."):
    abs_working = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(working_directory, directory))
    check_inside = os.path.exists(abs_target)
    check_dir = os.path.isdir(abs_target)
    if not check_inside:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not check_dir:
        return f'Error: "{directory}" is not a directory'
    
    try:
        list_files = []    
        for name in sorted(os.listdir(abs_target)):
            path = os.path.join(abs_target, name)
            size = os.path.getsize(path)
            is_dir = os.path.isdir(path)  
        
            list_files.append(f"- {name}: file_size={size} bytes, is_dir={is_dir}")
        output = "\n".join(list_files)    
        return output
    except Exception as e:
        return f"Error: {str(e)}"
    

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
    type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)