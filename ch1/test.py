import time
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

class MyTimer(object):
    def __init__(self, msg):
        self._msg = msg
    
    def __enter__(self):
        self._start_time = time.monotonic()
        return self._start_time

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            logger.info(f"{exc_type}, {exc_value}, {exc_traceback}")
        else:
            logger.info(f"{self._msg}: {time.monotonic() - self._start_time}")
        return True

with MyTimer("Hello") as v:
    logger.info(v)
    for i in range(300000):
        pass

    raise Exception("Sudden Exception!!")
