class Sample(object):
    
    def __init__(self):
        self.__x = 12
        self.__y = 3.1415
        self.__z = "str"

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x_in):
        self.__x = x_in

    @x.getter
    def x(self):
        return self.__x

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
    name = DescriptorExample()


# class 
# sample = Sample()
# print(sample.x)
# sample.x = 1000
# print(sample.x)

sample2 = Sample2()
print(sample2.name)
sample2.name = "Hello Hello"
print(sample2.name)
del sample2.name