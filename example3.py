import datetime

def log(func):
    #This records when you call a function with what specific arguments
    def wrapper(*args, **kwargs):
        with open("logs.txt", "a") as f:
            f.write("Called function with args" + " ".join([str(arg) for arg in args]) + " at " + str(datetime.datetime.now()) + "\n")
        val = func(*args, **kwargs)
        return val
    
    return wrapper


@log
def run(a, b, c=9):
    print(a+b+c)
    
run(1,3,c=9)