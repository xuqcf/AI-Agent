import os 

def get_files_info(working_directory, directory="."): 
    try:  
        path = os.path.abspath(working_directory)
        target_dir = os.path.abspath(
    os.path.normpath(os.path.join(working_directory, directory))
)


        
        valid_target_dir = os.path.commonpath([path, target_dir]) == path
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        lines = []

        for item in os.listdir(target_dir):
            item_path = os.path.join(target_dir, item)
            size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)

            lines.append(
                f"- {item}: file_size={size} bytes, is_dir={is_dir}"
            )
        return "\n".join(lines)
    except OSError as e:
        return f"Error: {e}"