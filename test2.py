from multipledispatch import dispatch

class OverloadingTest(object):

    @dispatch(int, int)
    def product(x, y):
        return x * y

    @dispatch(int, int, int)
    def product(x, y, z):
        return x * y * z

test = OverloadingTest()
print(test.product(10, 20))
print(test.product(10, 20, 30))

for t in int, float, list, tuple, type:
    print(f"{type(t)}")