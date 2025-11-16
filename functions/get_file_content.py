import os
def get_file_content(working_directory, file_path):
    abs_working = os.path.abspath(working_directory)
    abs_filepath = os.path.abspath(os.path.join(working_directory, file_path))
    check_inside = os.path.exists(abs_filepath)
    is_file = os.path.isfile(abs_filepath)
    
    if not check_inside:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not is_file:
        return f'Error: File not found or is not a regular file: "{file_path}"'
    return f"its working"
    # MAX_CHARS = 10000

    # with open(abs_target, "r") as f:
    #     file_content_string = f.read(MAX_CHARS)
print(get_file_content("calculator", "get_files_info.py"))
print(get_file_content("calculator", "main.py"))
print(get_file_content("calculator", "pkg/calculator.py"))
