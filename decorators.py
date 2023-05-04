# decorators are functions that takes another function as params, wrappes it in an inner func that performs that job that it has to do, and returns that inner function
# use when you want to change the behavior of a functin without modifying the func it's self
# @ it's decorator symbol 

def logtime(func):
    def wrapper():
        print('before')
        val = func()
        print('after')
        return val
    return wrapper


@logtime
def hello():
    print('Hello')

hello()