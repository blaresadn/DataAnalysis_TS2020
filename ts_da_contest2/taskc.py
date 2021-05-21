import signal
import functools


class TimeoutException(RuntimeError):
    def __init__(self, message=None):
        super().__init__(message)


def timeout(seconds=0.1):
    def decorator(func):
        if seconds is None or seconds <= 0:
            return func

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            def handler(signum, frame):
                raise TimeoutException("Timed out")

            old = signal.signal(signal.SIGALRM, handler)
            signal.setitimer(signal.ITIMER_REAL, seconds)
            result = func(*args, **kwargs)
            signal.setitimer(signal.ITIMER_REAL, 0)
            signal.signal(signal.SIGALRM, old)
            return result
        return wrapper
    return decorator
