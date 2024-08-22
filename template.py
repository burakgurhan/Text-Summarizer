import os
from pathlib import Path
import logging

# We will not create each file manually.
# This file automatically create  the basic template of the program.

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",   # We will use this file whenever we do CI/CD deployment to cloud.
    f"src/{project_name}/__init__.py",  
    f"src/{project_name}/components/__init__.py",  
    f"src/{project_name}/utils/common.py",  
    f"src/{project_name}/logging/__init__.py",  
    f"src/{project_name}/config/__init__.py",  
    f"src/{project_name}/config/configuration.py",  
    f"src/{project_name}/pipeline/__init__.py",  
    f"src/{project_name}/entity/__init__.py",  
    f"src/{project_name}/constants/__init__.py",  
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]


for filepath in list_of_files:
    filepath = Path(filepath)           # Make sure all paths are in a proper file path.
    
    # Split Fold name and file name
    filedir, filename = os.path.split(filepath)

    if filedir != "": # If there is no such fold.
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}.")

    if (not os.path.exists(filepath) or os.path.getsize(filepath)==0): # If there is no such file or it has 0 size.
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file {filepath}.")
    else:
        logging.info(f"{filename} is already exist.")