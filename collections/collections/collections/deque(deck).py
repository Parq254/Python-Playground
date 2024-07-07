import collections
from collections import deque

d = deque('hello')
d.appendleft('4')
d.popleft()
d.extend('1000')
d.rotate(-2)
print(d)
