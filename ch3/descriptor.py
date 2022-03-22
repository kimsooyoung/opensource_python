"""
Chapter 3
Python Advanced(3) - Descriptor(1)
Keyword - descriptor, set, get, del, property

"""
"""

디스크립터

1. 객체에서 서로다른 객체를 속성값으로 가지는 것.
2. Read, Write, Delete 등을 미리 정의 가능
3. data descriptor(set, del), non-data descriptor(get)
4. 읽기 전용 객체 생성 장점, 클래스를 의도하는 방향으로 생성 가능

"""

# Ex1
# 기본적인 Descriptor 예제
class DescriptorEx1(object): 
  
    def __init__(self, name = 'Default'): 
        self.name = name 
  
    def __get__(self, obj, objtype): 
        return "Get method called. -> self : {}, obj : {}, objtype : {}, name : {}".format(self, obj, objtype, self.name) 
  
    def __set__(self, obj, name):
        print('Set method called.')
        if isinstance(name, str): 
            self.name = name
        else:
            raise TypeError("Name should be string") 

    def __delete__(self, obj):
        print('Delete method called.')
        self.name = None


class Sample1(object): 
    name = DescriptorEx1()

s1 = Sample1()

# __set__ 호출 
s1.name = "Descriptor Test1"

# 예외 발생
# s1.name = 7

# attr 확인
# __get__ 호출
print('Ex1 > ', s1.name)

# __delete__ 호출
del s1.name

# 재확인
# __get__ 호출
print('Ex1 > ', s1.name)

print()
print()


# Ex2
# Property 클래스 사용 Descriptor 직접 구현
# class property(fget=None, fset=None, fdel=None, doc=None)

class DescriptorEx2(object): 
  
    def __init__(self, value): 
        self._name = value 
  
    def getVal(self): 
        return "Get method called. -> self : {}, name : {}".format(self, self._name) 
  
    def setVal(self, value): 
        print('Set method called.')
        if isinstance(value, str): 
            self._name = value
        else: 
            raise TypeError("Name should be string") 

    def delVal(self):
        print('Delete method called.')
        self._name = None

    name = property(getVal, setVal, delVal, 'Property Method Example.')  


s2 = DescriptorEx2('Descriptor Test2') 

# 최초 값 확인
print('Ex2 > ', s2.name)

# setVal 호출 
s2.name = "Descriptor Test2 Modified."

# 예외 발생
# s2.name = 10

# attr 확인
# getVal 호출
print('Ex2 > ', s2.name)

# delVal 호출
del s2.name

# 재확인
# getVal 호출
print('Ex2 > ', s2.name)

# doc 확인
print('Ex2 > ', DescriptorEx2.name.__doc__)

"""
Chapter 3
Python Advanced(3) - Descriptor(2)
Keyword - descriptor vs property, low level(descriptor) vs high level(property)

"""
"""

디스크립터

1. 상황에 맞는 메소드 구현을 통한 객체 지향 프로그래밍 구현
2. Property와 달리 reuse(재사용) 가능
3. ORM Framework 사용 : https://docs.python.org/ko/3/howto/descriptor.html#orm-example

"""

# Ex1
# Descriptor 예제(1)

import os

class DirectoryFileCount:
    def __get__(self, obj, objtype=None):
        # print(os.listdir(obj.dirname))
        return len(os.listdir(obj.dirname))

class DirectoryPath:
    # Descriptor instance
    size = DirectoryFileCount()             
    # Regular instance attribute
    def __init__(self, dirname):
        self.dirname = dirname          

# 현재 경로
s = DirectoryPath('./')
# 이전 경로 
g = DirectoryPath('../')

# 헷갈릴때 출력 용도
print('Ex1 > ', dir(DirectoryPath))
print('Ex1 > ', DirectoryPath.__dict__)
print('Ex1 > ', dir(s))
print('Ex1 > ', s.__dict__)

# 확인
print(s.size)
print(g.size)

# Ex2
# Descriptor 예제(2)

import logging

logging.basicConfig(
    format='%(asctime)s %(message)s',
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
print('Ex2 > ', s1.score)

# 점수 확인(s2)
print('Ex2 > ', s2.score)
s2.score += 20
print('Ex2 > ', s2.score)

# __dict__ 확인
print('Ex2 > ', vars(s1))
print('Ex2 > ', vars(s2))
print('Ex2 > ', s1.__dict__)
print('Ex2 > ', s2.__dict__)