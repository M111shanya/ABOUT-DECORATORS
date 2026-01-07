def outer(func):
    def inner(*args, **kwargs):
        print("Реклама епта!")
        return func(*args, **kwargs)
        
    return inner

def div(a, b):
    return a / b

var = outer(div)
print(type(var))
print(var(1, 2))