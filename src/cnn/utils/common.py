import os
from pathlib import Path
import yaml
import json
import joblib
import base64
from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError
from cnn import logger


@ensure_annotations


def read_yaml(path_yaml: Path) -> ConfigBox:
    try:
        with open(path_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                raise ValueError("YAML file is empty")
            logger.info(f"YAML file loaded successfully from {path_yaml}")
            return ConfigBox(content)  # Explicitly return the ConfigBox object
    except ValueError as ve:
        raise ValueError(f"Error while reading YAML: {ve}")
    except Exception as e:
        raise e

@ensure_annotations
def make_dir(path_dir:list,verbose=True):
    for path in path_dir:
        os.makedirs(path,exist_ok=True)
        if verbose:
          logger.info(f"directory created at {path}")



@ensure_annotations
def save_json(path:Path,data:dict):
    with open(path,"w"):
        json.dump(data,f,indent=4)
        logger.info(f"json file save at :{path}")



@ensure_annotations
def load_json(path:Path)->ConfigBox:
    with open(path,"r") as f:
        content=json.load(f)
    logger.info(f"json loaded from {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data:any,path:Path):
    joblib.dump(value=data,filename=path)
    logger.info(f"save bin at {path}")


@ensure_annotations
def load_bin(path:Path):
    data=joblib.load(path)
    logger.info(f"loaded bin file from {path}")
    return data

@ensure_annotations
def decode_image(imgstring,filename):
    imgdata=base64.b64decode(imgstring)
    with open(filename,"wb") as f:
        f.write(imgdata)
        f.close()


@ensure_annotations
def encode_image(imgpath):
    with open(imgpath,"rb") as f:
        return base64.b64.encode(f.read())
    

@ensure_annotations
def get_size(path: Path) -> str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

    

    