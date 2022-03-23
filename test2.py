import logging

logging.basicConfig(
    format='%(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

class LoggedScoreAccess:

    def __init__(self, value=60):
        self.value = value

    def __get__(self, obj, objtype=None):
        logging.info('Accessing %r giving %r', 'score', self.value)
        return self.value

    def __set__(self, obj, value):
        logging.info('Updating %r to %r', 'score', self.value)
        self.value = value

class Student:
    # Descriptor instance
    score = LoggedScoreAccess()          

    def __init__(self, name):
        # Regular instance attribute
        self.name = name                  


s1 = Student('Kim')
s2 = Student('Lee')

# 점수 확인(s1)
print('Ex2 > ', s1.score)
s1.score += 10
# print('Ex2 > ', s1.score)

# # 점수 확인(s2)
# print('Ex2 > ', s2.score)
# s2.score += 20
# print('Ex2 > ', s2.score)