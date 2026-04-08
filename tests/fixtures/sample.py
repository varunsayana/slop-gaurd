def real_function(*args, **kwargs):
    pass


def do_something():
    pass


def dummy_wrapper(*args, **kwargs):
    return real_function(*args, **kwargs)


def useless_empty():
    pass


try:
    do_something()
except Exception:
    pass
