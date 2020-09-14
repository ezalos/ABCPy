#__dict__ :
# A dictionary or other mapping object
# used to store an object's (writable) attributes.

class MyClass(object):
    class_var = 1

    def __init__(self, i_var):
        self.i_var = i_var

foo = MyClass(2)
bar = MyClass(3)

print(MyClass.__dict__)
print(foo.__dict__)
print(bar.__dict__)

def func():
    pass

func.temp = 1

print(func.__dict__)

class TempClass:
    a = 1
    def temp_function(self):
        pass

print(TempClass.__dict__)
