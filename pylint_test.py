import os
import subprocess

def run_pylint():
    """
    Run Pylint on all Python files in the current directory.
    """
    # Find all Python files in the current directory
    python_files = [file for file in os.listdir() if file.endswith('.py')]

    if not python_files:
        print("No Python files found.")
        return

    # Run Pylint on each Python file
    for python_file in python_files:
        # Construct the full path to the Python file
        file_path = os.path.join(os.getcwd(), python_file)

        # Run Pylint and capture the return code
        result = subprocess.run(['pylint', file_path])

        # Check the return code and handle it as needed
        if result.returncode != 0:
            print(f"Warning: Pylint returned a non-zero exit code for {python_file}.")

if __name__ == "__main__":
    run_pylint()
