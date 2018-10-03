def f(one=None, two=None, three=None):
    print(one, two, three)

def g(*args):
    print(args)

f([1, 2, 3])
f(*[1, 2, 3])

g([1, 2, 3])
g(1, 2, 3)
