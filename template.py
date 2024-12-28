import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_name="cnn"

file_list=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/config/config.yaml",
    "dvc.yaml",
    "setup.py",
    "params.yaml",
    "research/trials.ipynb",
    "templates/index.html",
    "main.py",
    "models"
    "requirements.txt"

    

]

for filepath in file_list:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"directory created:{filedir} for {filename}")

    if (not os.path.exists(filepath)):
        with open(filepath,"w") as f:
            pass
        logging.info(f"file  created {filepath}")

    else :
        logging.info(f" {filename} :files already exist")

    