import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    try:
        abs_working = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
        check_inside = abs_file_path.startswith(abs_working)
        is_file = os.path.isfile(abs_file_path)
    
        if not check_inside:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not is_file:
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(abs_file_path, "r") as f:
            file_content = f.read(MAX_CHARS)
            if os.path.getsize(abs_file_path) > MAX_CHARS:
                file_content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return file_content
    except Exception as e:
        return f"Error: {str(e)}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read file contents, constrained to the working directory.",
    parameters=types.Schema(
    type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

