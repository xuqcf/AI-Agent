import os, subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))
        if os.path.commonpath([abs_working_dir, abs_file_path]) != abs_working_dir: # If the file_path is outside the working_directory, return the error string below.
            return f'Cannot execute "{file_path}" as it is outside'
        if not os.path.isfile(abs_file_path): # If its not a regular file or if its not found it returns this error
            return f'"{file_path}" does not exist'
        if not abs_file_path.endswith('.py'):
            return f'"{file_path}" is not a Python file'

        
        command = ["python", abs_file_path]
        if args:
            command.extend(args)
        result = subprocess.run(command, text=True, capture_output=True, cwd=abs_working_dir, timeout=30)
        output_part = []
        
        if result.stdout.strip():
            output_part.append(f"STDOUT: {result.stdout.strip()}")

        if result.stderr.strip():
            output_part.append(f"STDERR: {result.stderr.strip()}")
        
        if not output_part:
            output_part.append("No output produced")
        
        if result.returncode != 0:
            output_part.append(f"Process exited with code {result.returncode}")

        output = "\n".join(output_part)
        return output
    except Exception as e:
        return f"Error: executing python file: {e}"