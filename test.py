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


test = DirectoryPath("./")

print('dir > ', dir(DirectoryPath))
print('__dict__ > ', DirectoryPath.__dict__)
print('dir > ', dir(test))
print('__dict__ > ', test.__dict__)