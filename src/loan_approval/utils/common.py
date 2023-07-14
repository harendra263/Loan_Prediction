import os
from box.exceptions import BoxValueError
import yaml
from loan_approval.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any, List


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads yaml file and returns

    Args:
        path_to_yaml(str): path like input
    
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    
    Returns:
        ConfigBox: ConfigBox Type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError("yaml file is empty") from e
    except Exception as e:
        raise e


@ensure_annotations
def create_dictionaries(path_to_directories: List, verbose=True):
    """
    create list of dictionaries

    Args:
        path_to_dictonaries(list): list of path of dictonaries
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def get_size(path: Path) ->str:
    """get size in kb
    
    Args:
        path (Path): path of the file
    
    Returns:
        str: size in kb
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} kb"
    
