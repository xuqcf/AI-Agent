import os 

def get_file_content(working_directory, file_path):
    try:
        path = os.path.abspath(working_directory)

        target_path = os.path.abspath(
        os.path.normpath(os.path.join(working_directory, file_path))
        )


        
        valid_target_dir = os.path.commonpath([path, target_path]) == path
        if not valid_target_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        MAX_CHARS = 10000
        with open(target_path, "r") as f:
            content = f.read(MAX_CHARS)

            if f.read(1): 
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'     
                return content
    except OSError as e:
        return f"Error: {e}"
