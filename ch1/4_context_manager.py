"""
Chapter 1
Python Advanced(1) - Context Manager(1) 
Keyword - Contextlib, __enter__, __exit__, exception

"""
"""
가장 대표적인 with 구문 이해
원하는 시점에 리소스 할당 및 회수
정확한 이해 후 사용 프로그래밍 개발 중요(문제 발생 요소)

"""

# Ex1
# No use with.

file = open('./testfile1.txt', 'w')
try:
    file.write('Context Manager Test1.\nContextlib Test1.')
finally:
    file.close()


# Ex2
# Use with.
with open('testfile2.txt', 'w') as f:
    f.write('Context Manager Test2.\nContextlib Test2.')

# Ex3
# Use Class -> Context Manager with exception handling
class MyFileWriter():
    def __init__(self, file_name, method):
        print('MyFileWriter started : __init__')
        self.file_obj = open(file_name, method)
        
    def __enter__(self):
        print('MyFileWriter started : __enter__')
        return self.file_obj

    def __exit__(self, exc_type, value, trace_back):
        print('MyFileWriter started : __exit__')
        if exc_type:
            print("Logging exception {}".format((exc_type, value, trace_back)))
        self.file_obj.close()

with MyFileWriter('testfile3.txt', 'w') as f:
    f.write('Context Manager Test3.\nContextlib Test3.')

"""
Chapter 1
Python Advanced(1) - Context Manager(2) 
Keyword - Contextlib, __enter__, __exit__

Contextlib - Measure execution(타이머) 제작
"""

# Ex1
# Use Class

import time

class ExcuteTimerCls(object):
    def __init__(self, msg):
        self._msg = msg

    def __enter__(self):
        self._start = time.monotonic()
        return self._start

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            print("Logging exception {}".format((exc_type, exc_value, exc_traceback)))
        else:
            print('{}: {} s'.format(self._msg, time.monotonic() - self._start))
        return True

with ExcuteTimerCls("Start! job") as v:
    print('Received start monotonic1 : {}'.format(v))
    # Excute job.
    for i in range(10000000):
        pass
    raise Exception("Raise! Exception.") # 강제로 발생

# My Example

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
            logger.info(f"{exc_value}, {exc_traceback}")
        else:
            logger.info(f"{self._msg}: {time.monotonic() - self._start_time}")
        return True

with MyTimer("Hello") as v:
    logger.info(v)
    for i in range(300000):
        pass

    # raise Exception("Sudden Exception!!")