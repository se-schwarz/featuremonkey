'''private helpers'''
import inspect
from functools import wraps

def _delegate(to):
    @wraps(to)
    def original_wrapper(throwaway, *args, **kws):
        return to(*args, **kws)

    return original_wrapper


def _is_class_instance(obj):
    return not inspect.isclass(obj) and not inspect.ismodule(obj)


def _get_role_name(role):
    if inspect.ismodule(role):
        return role.__name__
    return role.__class__.__name__


def _get_base_name(base):
    return "%s:%s" % (base.__name__, base.__class__.__name__)


def _get_method(method, base):
    if _is_class_instance(base):
        return method.__get__(base, base.__class__)
    else:
        return method