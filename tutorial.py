'''
Function Decorator tutorial

Use *args and **kwargs to pass parameters from g() to the wrapper function & the called function func()
'''
def f(func):
    def wrapper(*args, **kwargs):
        print("Started")
        func(*args, **kwargs)
        print("Ended")
    
    return wrapper

######################
# Function aliasing (Same core concept as decorating)
# def g():
#     print("Hello")

# x = f(g)
# x()
######################
# Decorated (writes "x = f(g)" using "@f" syntax)
# This calls the function g() and passes g() as a parameter to f()
@f
def g(a, b=9):
    print(a, b)
    
g("Hello")


'''
Returning values from decorated functions.
'''
def f1(func):
    def wrapper(*args, **kwargs):
        print("Started")
        val = func(*args, **kwargs)
        #extended logic here
        print("Ended")
        
        #return at the end
        return val
    
    return wrapper

@f1
def add(x,y):
    return x + y

res = add(25,7)
print(res)