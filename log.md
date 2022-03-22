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

여기서 주목할 점으로 DescriptorExample의 obj, objtype은 Sample2의 값이 나온다는 것이다. 자신이 포함된 클래스의 정보를 가져온다는 것임

Django 같은 거 쓰면, xx.yy 하면 DB에서 가져오는 이유가 이렇게 Descriptor class의 get 단에서 필요한 작업을 다해주기 때문이다.


Descriptor를 사용하는 두번째 방법 - property 함수 사용

```python
class PropertyClass(object):

    def __init__(self, name):
        self._name = name

    def getVal(self):
        print("getVal called")
        return self._name

    def setVal(self, value):
        print("setVal called")
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError("Invalid Data Type")
        
    def delVal(self):
        print("delVal called")
        self._name = None

    name = property(getVal, setVal, delVal, "Description")


test = PropertyClass("Hello")
print(test.getVal())
test.name = "Test Test"
print(test.getVal())
print(PropertyClass.name.__doc__)
del test.name

# 결과
getVal called
Hello
setVal called
getVal called
Test Test
Description
delVal called
```

이렇게 사용하면 obj, objtype 같은 것 없어도 되며, 함수 이름도 __get__이 아닌 임의의 함수명을 사용해도 된다.

사용법은 클래스의 마지막에 property 함수를 호출하면 된다.

getter, settter, del, __doc__ 순으로 들어간다.
`name = property(getVal, setVal, delVal, 'Property Method Example.')`

Descriptor 사용 전

![image](https://user-images.githubusercontent.com/12381733/159466580-9d88fe4d-1c85-4a91-a9ad-40a7d2dd18e2.png)

Descriptor 사용 후

![image](https://user-images.githubusercontent.com/12381733/159466597-6d1ba38e-a71e-47c1-9cec-cf30a3f3eb85.png)

일전 배운 new init call 이런 것들과 함께 사용하면 더 좋음
정말 유명한 것들은 다 이렇게 되어 있다고 한다.

# 디스크립터 vs Property
Keyword - descriptor vs property, low level(descriptor) vs high level(property)

1. 상황에 맞는 메소드 구현을 통한 객체 지향 프로그래밍 구현
2. Property와 달리 reuse(재사용) 가능
3. ORM Framework 사용 : https://docs.python.org/ko/3/howto/descriptor.html#orm-example

현 디렉토리 위치에서의 파일, 폴더들을 다루는 예시를 살펴보자.

```python
import os

class DirectoryFileCount:
    def __get__(self, obj, objtype=None):
        print(os.listdir(obj.dirname))
        return len(os.listdir(obj.dirname))

class DirectoryPath:
    # Descriptor instance
    size = DirectoryFileCount()             
    # Regular instance attribute
    def __init__(self, dirname):
        self.dirname = dirname          


# 현재 경로
s = DirectoryPath('./')
s.size
# 이전 경로 
g = DirectoryPath('../')
g.size

# 결과
['log.md', 'README.md', '.git', 'ch3', 'ch1', '예제파일', 'test.py', 'ch2', 'test2.py']
['TBCppExamples', 'go1', 'rb_unitree_legged_sdk', 'vi_example.cpp', 'lcm-1.4.0', 'unitree_legged_sdk', 'ros_controllers', 'a1_patrol', 'v1.4.0.tar.gz', 'opensource_python', 'gtsam.zip', 'gtsam-4.0.2']
```


__get__의 obj DirectoryFileCount 자신이 아니라 DirectoryFileCount를 사용하는, Descriptor를 사용하는 class가 된다는 점에 주목한다.

중요한 건 DirectoryFileCount 클래스가 재사용 가능하다는 것이다.

getter/setter를 대체하는 descriptor와 file count descriptor를 함께 사용해보았다.

```python
import os

class DirectoryFileCount(object):

    def __get__(self, obj, objtype = None):
        print(os.listdir(obj.dirname))
        return len(os.listdir(obj.dirname))

class StrDescriptor(object):

    def __init__(self, default="str"):
        self.name = default

    def __get__(self, obj, objtype=None):
        return self.name

    def __set__(self, obj, name):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError("Invalid Type Error")
    
    def __delete__(self, obj):
        del self.name

class DirectoryPath:

    test = DirectoryFileCount()

    def __init__(self, dirname="./"):
        self.dirname = StrDescriptor(dirname)

my_path = DirectoryPath()
my_path.dirname = "./ch1"
print(my_path.dirname)

my_path.test

# 결과
./ch1
['1_variable_scope.py', 'my.log', 'testfile3.txt', '3_shallow_copy_deep_copy.py', 'test.txt', '2_lambda_reduce_map_filter.py', 'test.py', '4_context_manager.py']
```

dir과 __dict__로 속성들을 모두 살펴보자.

```python
test = DirectoryPath("./")

print('dir > ', dir(DirectoryPath))
print('__dict__ > ', DirectoryPath.__dict__)
print('dir > ', dir(test))
print('__dict__ > ', test.__dict__)
```

dir 결과에서는 DirectoryFileCount가 드러나지 않는다.
dict로 하면 드러나며 여기에는 DirectoryFileCount, DirectoryPath 같은 것들이 확인된다.

![image](https://user-images.githubusercontent.com/12381733/159472084-4d0e0e5a-b2bd-40d6-b6b8-8ca2a886d540.png)

두번째 예제 - 로깅 

15:00

