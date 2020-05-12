#!/usr/bin/python3
"""Simple script for installing dotfiles

Usage:
    Define in `targets.yml` which files should be installed and where.
    Then just run this script `python install.py`

Dependences:
    pyyaml

"""

import os
import shutil
import logging
from pathlib import Path
from typing import Mapping, Union

import yaml

TargetsParams = Mapping[str, str]
TargetsType = Mapping[str, Union[str, TargetsParams]]

YAML_DIR_FIELD = "source_dir"
YAML_TARGETS_FIELD = "targets"

YAML_SRC = Path("targets.yml")
LOGGER = logging.getLogger()


def check_keys(file: TargetsType) -> bool:
    """Checks for keys in yaml file

    """
    exception_str = (
        f"File 'targets.yml' must include '{YAML_TARGETS_FIELD}' and '{YAML_DIR_FIELD}'"
    )
    restricted_set = {YAML_DIR_FIELD, YAML_TARGETS_FIELD}
    check_set = restricted_set.intersection(file.keys())
    if check_set != restricted_set:
        raise ValueError(exception_str)

    return True


def is_target_valid(filename: str, params: TargetsParams, src: Path) -> bool:
    """Checks whether target in yaml file valid

    """
    if not src.joinpath(filename).is_file():
        LOGGER.warning("WARNING: File is not exist: %s", filename)
        return False
    if "dir" not in params:
        LOGGER.warning(
            "WARNING: Target must include 'dir' and optionally 'filename': %s", filename
        )
        return False

    return True


def mkdir_recursive(directory: Path):
    """Makes directory with recursion

    """
    if directory.is_dir():
        return
    mkdir_recursive(directory.parent)
    directory.mkdir()


def make_dest_path(params: TargetsParams, name: str) -> Path:
    """Makes destination path from target paramters

    """
    res_dir = Path(os.path.expandvars(params["dir"])).absolute()

    if "filename" in params:
        res_path = res_dir / params["filename"]
    else:
        res_path = res_dir / name

    return res_path


if __name__ == "__main__":
    with YAML_SRC.open() as f:
        try:
            targets: TargetsType = yaml.safe_load(f)
        except yaml.YAMLError as ex:
            print(ex)

    check_keys(targets)
    SRC_DIR = Path(targets[YAML_DIR_FIELD])

    for target, parameters in targets[YAML_TARGETS_FIELD].items():
        if is_target_valid(target, parameters, SRC_DIR):
            dest = make_dest_path(parameters, target)
            if not dest.parent.is_dir():
                mkdir_recursive(dest.parent)
            shutil.copy(SRC_DIR / target, dest)
        else:
            print(f"Target '{target}' is not proccessed")

    print("Done!")
