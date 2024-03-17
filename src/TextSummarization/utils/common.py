import os 
from box.exceptions import BoxValueError
from yaml
from src.TextSummarization.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

#dict has not attribute, with box, you can access the value by attribute

#decorator to ensure annotations are used in the function, because ensure_annotations is not a built-in function
#ensure_annotations is a decorator that checks if the function is annotated with type hints

@ensure_annotations
def read_yaml(filepath: Path) -> ConfigBox:
    """read yaml file and return

    Args:
      filepath(str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file
    
    Returns:
        ConfigBox: ConfigBox type

    """

    try:
        with open(filepath, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {filepath} is read successfully")
            return ConfigBox(content)
    
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

def create_directories(path_to_dir: list, verbose = True): 
    """
    Create list of directories

    Args:
      path_to_dir(list): list of directories
      verbose(bool): print message if True
      ignore_log (bool, optional): ignore if multible dirs is to be created. Defaults to False.

    """
    for path in path_to_dir:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Creating directory: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """get size of file in KB

    Args:
      path(Path): path of file

    Returns:
      Any: size of file in KB

    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"{size_in_kb} KB"