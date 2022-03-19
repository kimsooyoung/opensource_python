"""
Chapter 3
Python Advanced(3) - Meta Class(1)
Keyword - Class of Class, Type, Meta Class, Custom Meta Class

"""
"""

메타클래스
1. 클래스를 만드는 역할 -> 의도하는 방향으로 클래스 커스텀
2. 프레임워크 작성 시 필수
3. 동적 생성(type함수), 커스텀 생성(type상속)
4. 커스텀 클래스 -> 검증클래스 등
5. 엄격한 Class 사용 요구, 메소드 오버라이드 요구

"""

# Ex1
# type 예제


class SampleA:  # Class == Object
    pass


obj1 = SampleA()  # 변수에 할당, 복사 가능, 새로운 속성, 함수의 인자로 넘기기 가능

# obj1 -> SampleA instance
# SampleA -> type metaclass
# type -> type metaclass
print("Ex1 > ", obj1.__class__)
print("Ex1 > ", type(obj1))
print("Ex1 > ", obj1.__class__ is type(obj1))

print()


# Ex2
# type meta (Ex1 증명)

# int, dict 선언
n = 10
d = {"a": 10, "b": 20}


class SampleB:
    pass


obj2 = SampleB()

for o in (n, d, obj2):
    print(
        "Ex2 >  {} {} {}".format(type(o), type(o) is o.__class__, o.__class__.__class__)
    )


print()

# the type of any new-style class is type.
print(type(SampleA))
print(type(obj2))

print()

for t in int, float, dict, list, tuple:
    print("Ex2 > ", type(t))

print("Ex2 > ", type(type))

"""
Chapter 3
Python Advanced(3) - Meta Class(2)
Keyword - Type(name, base, dct), Dynamic metaclass

"""
"""

메타클래스
1. 메타클래스 동적 생성 방법 중요
2. 동적 생성 한 메타클래스 -> 커스텀 메타클래스 생성
3. 의도하는 방향으로 직접 클래스 생성에 관여 할 수 있는 큰 장점

"""

# Ex1
# type 동적 클래스 생성 예제

# Name(이름), Bases(상속), Dct(속성,메소드)
s1 = type("sample1", (), {})

print("Ex1 > ", s1)
print("Ex1 > ", type(s1))
print("Ex1 > ", s1.__base__)
print("Ex1 > ", s1.__dict__)

print()

# 동적 생성 + 상속
class Parent1:
    pass


s2 = type("Sample2", (Parent1,), dict(attr1=100, attr2="hi"))

print("Ex1 > ", s2)
print("Ex1 > ", type(s2))
print("Ex1 > ", s2.__base__)
print("Ex1 > ", s2.__dict__)
print("Ex1 >", s2.attr1, s2.attr2)

print()

# Ex2
# type 동적 클래스 생성 + 메소드


class SampleEx:
    attr1 = 30
    attr2 = 100

    def add(self, m, n):
        return m + n

    def mul(self, m, n):
        return m * n


ex = SampleEx()

print("Ex2 >", ex.attr1)
print("Ex2 >", ex.attr2)
print("Ex2 >", ex.add(100, 200))
print("Ex2 >", ex.mul(100, 20))
print()

# SampleEx 클래스를 Type 으로 동적 생성

s3 = type(
    "Sample3",
    (object,),  # 생략 가능
    dict(attr1=30, attr2=100, add=lambda x, y: x + y, mul=lambda x, y: x * y)
    # {'attr1': 30, 'attr2': 100, 'add': lambda x, y: x + y, 'mul': lambda x, y: x * y}
)

print("Ex2 >", s3.attr1)
print("Ex2 >", s3.attr2)
print("Ex2 >", s3.add(100, 200))
print("Ex2 >", s3.mul(100, 20))
print()

"""
Chapter 3
Python Advanced(3) - Meta Class(3)
Keyword - Type inheritance, Custom metaclass

"""
"""
 
메타클래스 상속
1. type클래스 상속
2. metaclass 속성 사용
3. 커스텀 메타 클래스 생성
   - 클래스 생성 가로채기(intercept)
   - 클래스 수정하기(modify)
   - 클래스 개선(기능추가)
   - 수정된 클래스 반환

"""

# Ex1
# 커스텀 메타클래스 생성 예제(Type 상속X)


def cus_mul(self, d):
    for i in range(len(self)):
        self[i] = self[i] * d


def cus_replace(self, old, new):
    while old in self:
        self[self.index(old)] = new


# list를 상속받음, 메소드 2개 추가
CustomList1 = type(
    "CustomList1",
    (list,),
    {"desc": "커스텀 리스트1", "cus_mul": cus_mul, "cus_replace": cus_replace},
)

c1 = CustomList1([1, 2, 3, 4, 5, 6, 7, 8, 9])
c1.cus_mul(1000)
c1.cus_replace(1000, 7777)

print("Ex1 > ", c1)
print("Ex1 > ", c1.desc)

print()


# Ex2
# 커스텀 메타클래스 생성 예제(Type 상속O)

# class MetaClassName(type):
#    def __new__(metacls, name, bases, namespace):
#        코드

# new -> init -> call 순서
class CustomListMeta(type):
    # 생성된 인스턴스 초기화
    def __init__(self, object_or_name, bases, dict):
        print("__init__ -> ", self, object_or_name, bases, dict)
        super().__init__(object_or_name, bases, dict)

    # 인스턴스 실행
    def __call__(self, *args, **kwargs):
        print("__call__ -> ", self, args, kwargs)

        return super().__call__(*args, **kwargs)

    # 클래스 인스턴스 생성(메모리 초기화)
    def __new__(metacls, name, bases, namespace):
        print("__new__ -> ", metacls, name, bases, namespace)
        namespace["desc"] = "커스텀 리스트2"
        namespace["cus_mul"] = cus_mul
        namespace["cus_replace"] = cus_replace

        return type.__new__(metacls, name, bases, namespace)


CustomList2 = CustomListMeta("CustomList2", (list,), {})

c2 = CustomList2([1, 2, 3, 4, 5, 6, 7, 8, 9])
c2.cus_mul(1000)
c2.cus_replace(1000, 7777)

print("Ex2 > ", c2)
print("Ex2 > ", c2.desc)

# 상속 확인
print(CustomList2.__mro__)
