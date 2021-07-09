def gen1(_l: list):
    for i in _l:
        yield i

g = gen1([1,2,3,4,5,])

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
