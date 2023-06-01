import importlib as _importlib
from types import ModuleType as _ModuleType
import sys as _sys
import os as _os

def reload_module(module: _ModuleType):
    _importlib.reload(module)

def import_from(folder: str, module: str):
    try:
        path = _os.path.abspath(folder)
        _sys.path.insert(1, path)

        _importlib.import_module(module)
    finally:
        _sys.path.remove(path)