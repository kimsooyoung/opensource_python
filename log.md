메타클래스

1. 클래스를 만드는 역할 -> 의도하는 방향으로 클래스 커스텀
2. 프레임워크 작성 시 필수
3. 동적 생성(type함수), 커스텀 생성(type상속)
4. 커스텀 클래스 -> 검증클래스 등
5. 엄격한 Class 사용 요구, 메소드 오버라이드 요구

파이썬에서는 클래스 = 객체 (Class = Object)라고 생각하면 된다.

```python
class Sample():
    pass

sample = Sample()
```

sample = Sample()하는 이 시점에 클래스가 인스턴스화 되고, 메모리에 올라간다.

Sample 클래스의 타입을 알아내는 방법은 두가지가 있다.

```python
class Sample:
    pass


sample = Sample()

print(sample.__class__)
print(type(sample))

# 결과
<class '__main__.Sample'>
<class '__main__.Sample'>
```

**class**를 사용하거나, type 함수를 사용하면 된다.
그런데, Sample 자체는 어떻게 만들어질까?

```python
class Sample:
    pass
sample = Sample()

print(sample.__class__.__class__)

# 결과
<class 'type'>
```

파이썬에서 type은 모든 클래스의 원형(meta)이 된다.

이 type을 사용하면 원하는 클래스를 임의로 만들 수도 있고 클래스 내 메소드, 변수를 동적으로 제어할 수 있는 것이다.

type의 type은 뭘까?

```python
print(type(type))

# 결과
<class 'type'>
```

=> type의 meta는 type이다.

obj1은 SampleA의 instance
type은 SampleA의 metaclass
type은 type의 metaclass

type이 어떻게 되어있는지는 파이썬 언어 단에서 cpython으로 되어 있는 것이고 언어 자체가 만들어지는 레벨에서 처리된다.

파이썬에서 모든 것들은 Object이고 Class이며, 이들의 metaclass는 모두 type이다.

```python
n = 10
d = {"a": 10, "b": 20}


class SampleB:
    pass


obj2 = SampleB()

for o in (n, d, obj2):
    print(
        "Ex2 >  {} {} {}".format(type(o), type(o) is o.__class__, o.__class__.__class__)
    )

# 결과
Ex2 >  <class 'int'> True <class 'type'>
Ex2 >  <class 'dict'> True <class 'type'>
Ex2 >  <class '__main__.SampleB'> True <class 'type'>
```

다시 한 번, 모든 것들의 meta는 type!!

```
for t in int, float, list, tuple, type:
    print(f"{type(t)}")
```

type 함수를 다루기

메타클래스

1. 메타클래스 동적 생성 방법 중요
2. 동적 생성 한 메타클래스 -> 커스텀 메타클래스 생성
3. 의도하는 방향으로 직접 클래스 생성에 관여 할 수 있는 큰 장점

type 함수는 3개의 매개변수를 받는다.

Type(name, base, dct) # Name(이름), BasesTuple(상속), Dct(속성,메소드)

```python
s1 = type("sample1", (), {})

print("Ex1 > ", s1)

# 결과
Ex1 >  <class '__main__.sample1'>
```

클래스를 생성하였다. 이는 class XXX 로 생성한 것과 완전 동일한 것임!

```python
s1 = type("sample1", (), {})

print("Ex1 > ", s1)
print("Ex1 > ", type(s1))
print("Ex1 > ", s1.__base__)

# 결과
Ex1 >  <class '__main__.sample1'>
Ex1 >  <class 'type'>
Ex1 >  <class 'object'>
```

s1의 type은 type이고, 모든 클래스는 object를 상속받기 때문에 base class는 object가 된다.

- 동적으로 클래스를 생성하면서 상속까지 시키기

```python
class Parent1:
    pass


s2 = type("Sample2", (Parent1,), dict(attr1=100, attr2="hi"))
```

dict 함수로 딕셔너리 생성한 것은 순전히 편의를 위한 것임

위 작업은 사실 이것과 동일하다.

```python
class Parent1:
    pass


class Sample(Parent1):
    attr1 = 12
    attr2 = "test"
```

동적 생성한 인스턴스의 여러 속성들을 확인해보자.

```python
class Parent1:
    pass


s2 = type("Sample", (Parent1,), dict(attr1=12, attr2="test"))

print("Ex1 > ", s2)
print("Ex1 > ", type(s2))
print("Ex1 > ", s2.__base__)
print("Ex1 > ", s2.__dict__)
print("Ex1 >", s2.attr1, s2.attr2)

# 결과
Ex1 >  <class '__main__.Sample'>
Ex1 >  <class 'type'>
Ex1 >  <class '__main__.Parent1'>
Ex1 >  {'attr1': 12, 'attr2': 'test', '__module__': '__main__', '__doc__': None}
Ex1 > 12 test
```

동적으로 메소스도 만들어보자.

아래와 같은 클래스를 동적으로 생성하고 싶다.

```python
class SampleEx:
    attr1 = 30
    attr2 = 100

    def add(self, m, n):
        return m + n

    def mul(self, m, n):
        return m * n
```

```python
s3 = type(
    "Sample",
    (object,),
    dict(attr1=30, attr2=100, add=lambda x, y: x + y, mul=lambda x, y: x * y),
)

print("Ex2 >", s3.attr1)
print("Ex2 >", s3.attr2)
print("Ex2 >", s3.add(100, 200))
print("Ex2 >", s3.mul(100, 20))
print()
```

현재 상속받는 것이 없지만, 두번째 인자로 object를 명시해도 된다.

메소드를 전달해줄 때 람다를 사용하면 편하다.

메타클래스 상속

1. type클래스 상속
2. metaclass 속성 사용
3. 커스텀 메타 클래스 생성
   - 클래스 생성 가로채기(intercept)
   - 클래스 수정하기(modify)
   - 클래스 개선(기능추가)
   - 수정된 클래스 반환

type클래스를 상속 한다는 것은 곧 메타클래스를 상속한다는 것이다.

커스텀 메타클래스 생성 기초

```python
def cus_mul(self, d):
    for i in range(len(self)):
        self[i] *= d


def cus_replace(self, old, new):
    for i in range(len(self)):
        if self[i] == old:
            self[i] = new


CustomList1 = type(
    "CustomList",
    (list,),
    dict(cus_mul=cus_mul, cus_replace=cus_replace),
)

sample = CustomList1()
print(sample)
sample.cus_mul(100)
print(sample)

sample2 = CustomList1([i for i in range(10)])
print(sample2)
sample2.cus_mul(100)
print(sample2)

# 결과
[]
[]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 100, 200, 300, 400, 500, 600, 700, 800, 900]
```

self라는 것은 초기화 시 유입되는 매개변수를 가리키게 된다.

따라서 매개변수 없이 CustomList1() 이렇게만 호출하면 cus_mul는 list를 상속받았으므로 빈 list가 들어가게 된다.

이렇게 필요할 법한 함수들을 다 구현해두고, 실제 클래스를 만들 떄는 동적으로 함수들을 조합하여 사용할 수 있다.

구현한 함수 중 cus_replace도 실습해보자.

```python
sample2 = CustomList1([i for i in range(10)])
print(sample2)
sample2.cus_replace(5, "안녕")
print(sample2)

# 결과
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, '안녕', 6, 7, 8, 9]
```

지금 list를 상속받아서 그 위에 커스텀 함수를 구현한 것임을 명심하자.

이번에는 type 클래스를 상속받아 커스터마이징을 해보자.

```python
class CustomListMeta(type):
```

이렇게 type을 상속받으면, **call**, **init**, **new**와 같은 매직 메소드들을 사용할 수 있게 된다.

실행 순서는 new => init => call 이다.
(지금 하는 이 작업은 매우 deep 한 것임)

new 함수에서 인스턴스가 생성되고, 메모리가 할당된다.

new 함수는 metacls, name, bases, namespace 3개의 매개변수를 받는다.
그리고 이들은 일전 type 함수 호출로 클래스 생성 시 전달했던 3개의 매개변수와 동일하다.

```python
CustomList1 = type(
    "CustomList", # => name
    (list,), # => bases
    dict(cus_mul=cus_mul, cus_replace=cus_replace), # => namespace
)
```

new의 namespace를 통해 원하는 변수와 함수를 만들 수 있다.
new는 반드시 return을 해야 한다.

```python
def __new__(metacls, name, bases, namespace):
    print("__new__ -> ", metacls, name, bases, namespace)
    namespace["desc"] = "커스텀 리스트2"
    namespace["cus_mul"] = cus_mul
    namespace["cus_replace"] = cus_replace

    return type.__new__(metacls, name, bases, namespace)
```

init 함수는 3개의 매개변수를 받고, 이는 type 함수로 클래스 생성 시의 매개변수들과 동일하다.
init 단에서 invariant를 적용하여 조건을 추가할 수 있을 것이다.

```python
def __init__(self, object_or_name, bases, dict):
```

type을 상속받아 구현중이므로 `super().__init__`을 통해 type에게 전달하고 있다.

call 함수는 일반 함수의 매개변수와 동일하게 값이 전달된다.
왜 args, kwargs냐? 파이썬이 원래 그럼

```python
def __call__(self, *args, **kwargs):
```

정리하자면, type을 사용해서 함수 형태로 바로 클래스를 생성할 수도 있고, type을 상속받는 클래스를 구현해서 new, init, call과 같은 심화된 커스터마이징을 할 수도 있다.

직접 실행하며 실습해보자.

```python
def cus_mul(self, d):
    for i in range(len(self)):
        i *= d


def cus_replace(self, old, new):
    for num, val in enumerate(self):
        if val == old:
            self[num] = new


class MyMetaClass(type):
    def __new__(metacls, name, bases, namespace):
        print(f"__new__ {metacls}, {name}, {bases}, {namespace}")
        namespace["cus_mul"] = cus_mul
        namespace["cus_replace"] = cus_replace

        return type.__new__(metacls, name, bases, namespace)

    def __init__(self, name, bases, namespace):
        print(f"__init__ {self} {name}, {bases}, {namespace}")
        super().__init__(name, bases, namespace)

    def __call__(self, *args, **kwargs):
        print(f"__call__ {self} {args}, {kwargs}")
        return super().__init__(*args, **kwargs)


MyCls = MyMetaClass(
    "MyMetaClass", (list,), dict(cus_mul=cus_mul, cus_replace=cus_replace)
)

# 결과
__new__ <class '__main__.MyMetaClass'>, MyMetaClass, (<class 'list'>,), {'cus_mul': <function cus_mul at 0x7fc98e8bb160>, 'cus_replace': <function cus_replace at 0x7fc990825b80>}
__init__ <class '__main__.MyMetaClass'> MyMetaClass, (<class 'list'>,), {'cus_mul': <function cus_mul at 0x7fc98e8bb160>, 'cus_replace': <function cus_replace at 0x7fc990825b80>}
```

새로운 클래스를 만들어주는 순간, new, init이 호출된다.

```python
mycls = MyCls([1, 2, 3, 4, 5, 6])

# 결과
__call__ <class '__main__.MyMetaClass'> ([1, 2, 3, 4, 5, 6],), {}
```

인스턴스를 만드눈 순간에 call이 실행된다.

클래스 상속 구조를 파악하는 방법 (**mro** )

```python
print(MyCls.__mro__)
# (<class '__main__.MyMetaClass'>, <class 'list'>, <class 'object'>)
```
