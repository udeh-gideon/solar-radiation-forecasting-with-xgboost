import os
from box.exceptions import BoxValueError
import yaml
from src.solar_radiation_prediction import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    '''
    Reads yaml file and returns

    Args:
        path_to_yaml (str): Path like input
    
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    
    Returns:
        ConfigBox: ConfigBox type
    '''

    try:
        with open(path_to_yaml) as yaml_file:
            content =  yaml.safe_load(yaml_file)
            logger.info(f'yaml file: {path_to_yaml} loaded successfully')
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f'yaml file: {path_to_yaml} is empty')
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    '''
    create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    '''

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f'directory created at: {path}')

@ensure_annotations
def save_json(path: Path, data: dict):
    '''
    Save json file

    Args:
        path (str): path to save json file
        data (dict): data to be saved
    
    Returns:
        ConfigBox: data as class attributes instead of dictionary
    '''
    with open(path) as f:
        content = json.load(f)
    
    logger.info(f'json file: {path} loaded successfully')
    return ConfigBox(content)

@ensure_annotations
def save_bin(path: Path, data: Any):
    '''
    Save binary data

    Args:
        path (str): path to save binary file
        data (Any): data to be saved
    '''
    joblib.dump(value=data, filename=path)
    logger.info(f'binary file: {path} saved successfully')

@ensure_annotations
def load_bin(path: Path) -> Any:
    '''
    Load binary data

    Args:
        path (str): path to binary file

    Returns:
        Any: object stored in the file
    '''
    data = joblib.load(path)
    logger.info(f'binary file: {path} loaded successfully')
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    '''
    Get size of the file in KB

    Args:
        path (str): path to file

    Returns:
        int: size of the file
    '''
    size_in_kb = round(os.path.getsize(path)/1024)
    return f'file size: {size_in_kb} KB'