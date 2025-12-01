# python
from functions.get_files_info import  schema_get_files_info,get_files_info
from functions.get_file_content import schema_get_file_content,get_file_content
from functions.run_python_file import run_python_file, schema_run_python_file
from functions.write_file import schema_write_file,write_file

def main():
    print(get_file_content({'file_path': 'main.py'}) )
    print(write_file({'file_path': 'main.txt', 'content': 'hello'}))
    print(run_python_file({'file_path': 'main.py'}))
    print(get_files_info({'directory': 'pkg'})) 
    

if __name__ == "__main__":
    main()