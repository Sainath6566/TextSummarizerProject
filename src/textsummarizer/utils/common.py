import os
import yaml
from textsummarizer.logging import logger
from pathlib import Path
from typing import Any



def read_yaml(path_to_yaml: Path) -> Any:
    """
    reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        dict: Content of the YAML file as a dictionary
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return content
    except Exception as e:
        raise e



def create_directories(path_to_directories: list, verbose=True):
    """
    create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for Path in path_to_directories:
        os.makedirs(Path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {Path}")




def get_size(path: Path) -> str:
    """
    get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.Path.getsize(Path)/1024)
    return f"~ {size_in_kb} KB"

    