import functools


def catch_them_all(f):
    @functools.wraps(f)
    def inhandler(*args, **kwargs):
        semaphore = False
        try:
            return f(*args, **kwargs)
        except Exception:
            semaphore = True
        finally:
            if semaphore:
                print('Function worked well')
    return inhandler


@catch_them_all
def e_func():
    raise Exception('Exception executed!')


e_func()
