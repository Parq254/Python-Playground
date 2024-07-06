'''
def func(x):
    func2 = lambda x: x+5
    return func2(x) + 85

func3 = lambda x,y: x+y
print(func3(5,5))

print(func(2))
'''

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newlist = list(map(lambda x: x+5,a))
print(newlist)