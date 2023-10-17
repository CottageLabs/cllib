import importlib
from typing import Optional, Any

load_module = importlib.import_module


def load_module_obj(obj_path) -> Optional[Any]:
    *modules, obj_name = obj_path.split(".")
    modpath = ".".join(modules)
    try:
        mod = importlib.import_module(modpath)
    except ImportError:
        return None
    fn = getattr(mod, obj_name, None)
    return fn
