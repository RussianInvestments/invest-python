from functools import wraps

import pytest


def skip_when(
    exception_type,
    is_error_message_expected,
    reason="Skipping because of the exception",
):
    def decorator_func(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except exception_type as error:
                if is_error_message_expected(str(error)):
                    pytest.skip(reason)
                else:
                    raise error

        return wrapper

    return decorator_func
