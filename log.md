Descriptor

1. 객체에서 서로다른 객체를 속성값으로 가지는 것.
2. Read, Write, Delete 등을 미리 정의 가능
3. 데이터를 실제로 다루는 작업 - data descriptor(set, del) 그렇지 않은 것 - non-data descriptor(get)
4. 읽기 전용 객체 생성 장점, 클래스를 의도하는 방향으로 생성 가능

getter, setter와 비슷하지만 좀 더 raw level인 것이 다르다.

사용 방법

```python
def __get__(self, obj, objtype): 
    return sth
...
def __set__(self, obj, name):
    invariant 삽입 가능
...
def __delete__(self, obj):
```

일전 property를 사용하면 모든 클래스 변수마다 @property, @xx.getter, @xx.setter를 붙여야 했다. descriptor class를 사용하면 이러한 번거로움을 줄일 수 있음

```python
class DescriptorExample(object):

    def __init__(self, default="Default"):
        self.name = default

    def __get__(self, obj, objtype): 
        print("__get__")
        print(f"{self} {obj} {objtype}")
        return self.name
        
    def __set__(self, obj, name):
        print("__set__")
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError("Invalid Value Err")

    def __delete__(self, obj):
        print("__del__")
        self.name = None
        
class Sample2(object):
    str_name1 = DescriptorExample()
    str_name2 = DescriptorExample()
    str_name3 = DescriptorExample()
    str_name4 = DescriptorExample()
    ...
```

여기서 나온 isinstance 함수 잘 알아두자.

```
print(isinstance("213", str))
# 결과 -> True
```

예제 실행
```python
sample2 = Sample2()
print(sample2.name)
sample2.name = "Hello Hello"
print(sample2.name)
del sample2.name

# 결과
__get__
<__main__.DescriptorExample object at 0x7f21d650b9e8> <__main__.Sample2 object at 0x7f21d650ba20> <class '__main__.Sample2'>
Default
__set__
__get__
<__main__.DescriptorExample object at 0x7f21d650b9e8> <__main__.Sample2 object at 0x7f21d650ba20> <class '__main__.Sample2'>
Hello Hello
__del__
```

Django 같은 거 쓰면, xx.yy 하면 DB에서 가져오는 이유가 이렇게 Descriptor class의 get 단에서 필요한 작업을 다해주기 때문이다.


Descriptor를 사용하는 두번째 방법 - property 함수 사용

```python

```

이렇게 사용하면 obj, objtype 같은 것 없어도 되며, 함수 이름도 __get__이 아닌 임의의 함수명을 사용해도 된다.

사용법은 클래스의 마지막에 property 함수를 호출하면 된다.

getter, settter, del, __doc__ 순으로 들어간다.
`name = property(getVal, setVal, delVal, 'Property Method Example.')`


