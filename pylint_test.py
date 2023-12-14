import os
import subprocess

def run_pylint():
    # Find all Python files in the current directory
    python_files = [file for file in os.listdir() if file.endswith('.py')]

    if not python_files:
        print("No Python files found.")
        return

    # Run Pylint on each Python file
    for python_file in python_files:
        subprocess.run(['pylint', python_file])

if __name__ == "__main__":
    run_pylint()
