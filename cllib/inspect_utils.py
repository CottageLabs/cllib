import inspect


def issubclass_safe(target_cls, check_cls):
    if not target_cls or not inspect.isclass(target_cls):
        return False

    return issubclass(target_cls, check_cls)


def get_fn_path(fn):
    module = inspect.getmodule(fn)
    module_name = module.__name__ if module else ''
    fn_name = fn.__name__

    return f'{module_name}.{fn_name}' if module_name else fn_name
