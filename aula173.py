# count - Iterador sem fim
from itertools import count

c1 = count(50, 20)
r1 = range(2)


print('c1', hasattr(c1, '__iter__')) # É iteravel?
print('c1', hasattr(c1, '__next__')) # É Iterator?
print('c1', hasattr(r1, '__iter__'))
print('c1', hasattr(r1, '__next__'))



print(next(c1))
print(next(c1))
print(next(c1))
print(next(c1))
print(next(c1))
print(next(c1))

print(r1)

