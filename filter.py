def add7(x):
    return x + 7


def isodd(x):
    return True


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = list(filter(isodd, a))
c = list(map(add7, filter(isodd, a)))
print(c)

