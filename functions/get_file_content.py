import os
def get_file_content(working_directory, file_path):
    abs_working = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(working_directory, file_path))
    check_inside = os.path.commonpath([abs_working, abs_target]) == abs_working
    is_file = os.path.isfile(abs_target)
    if not check_inside:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not is_file:
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
