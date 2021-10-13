from contextlib import contextmanager


@contextmanager
def file_handler(file_name, file_mode):
    try:
        f = open(file_name, file_mode)
        yield f
    except OSError:
        print("Something went wrong")
    finally:
        f.close()


with file_handler("test_x.txt", "w") as f:
    f.write("Test string")

