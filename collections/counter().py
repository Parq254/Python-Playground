import collections
from collections import Counter
'''
c = Counter('glad')
print(c)
c = Counter(['a','a','b','c','c'])
print(c)
c = Counter({'a':1, 'b':2})
print(c)
c = Counter(cats=4, dogs=7)
print(c)
'''

'''
c = Counter(a=4, b=2, c=0, d=-2)
d = ['a', 'b', 'b', 'c']
c.subtract(d)
print(c)
'''

c = Counter([1, 1, 1, 3, 4, 5, 6, 7, 7])
feedback = c.most_common(1)
print(feedback)
