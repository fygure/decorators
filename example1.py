import time

def before_after(func):
    def wrapper(*args):
        print("Before")
        func(*args)
        print("After")
        
    return wrapper

class Test:
    @before_after
    def decoratedd_method(self):
        print("running")

t = Test()
t.decoratedd_method()