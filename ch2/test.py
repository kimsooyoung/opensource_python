import time
import logging
import contextlib

from pkg_resources import yield_lines

@contextlib.contextmanager
def timer_context(msg):
    msg = msg
    start = time.monotonic()

    try:
        yield start
    except Exception as e:
        print(e)
    finally:
        print(msg, time.monotonic() - start)

with timer_context("Hello") as v:
    for i in range(300000):
        pass
    
    raise Exception("test")