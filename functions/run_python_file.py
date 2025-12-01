import os
import subprocess
from google.genai import types
def run_python_file(working_directory, file_path, args=[]):
    try:
        abs_working = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
        check_inside = abs_file_path.startswith(abs_working)
        if not check_inside:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(abs_file_path):
            return f'Error: File "{file_path}" not found.'
        if not file_path.endswith('.py'):
            return f'Error: File "{file_path}" is not a Python file.'
        subpro = subprocess.run(timeout=30,capture_output=True,args=['python', abs_file_path]+args,text=True,cwd = abs_working)
        STDOUT = subpro.stdout
        STDERR = subpro.stderr
        output = ""
        if STDOUT:
            output += f"Output:\n{STDOUT}"
        if STDERR:
            output += f"Errors:\n{STDERR}"
        if subpro.returncode != 0:
            output += f"\nProcess exited with code {subpro.returncode}"
        return output
        if output == "":
            return "No output produced."
    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute Python files with optional arguments, constrained to the working directory.",
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


