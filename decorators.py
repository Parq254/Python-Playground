def logtime(func):
    def wrapper():
        print('Hello')
        val = func()
        print('Goodbye')
        return val
    return wrapper