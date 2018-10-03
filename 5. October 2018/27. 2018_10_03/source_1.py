import random

def rand_double(a, b):
    return random.random() * (b - a) + a

def linear(x, k=None, b=None):
    if k is None:
        k = random.uniform(-10, 10)
    if b is None:
        b = random.uniform(-20, 20)
    print('y = {} * x + {}'.format(k, b))
    return k * x + b

funcs = [
    lambda x: 2 * x - 3,
lambda x: -5 * x + 2,
lambda x: 6 * x - 1
    ]

f = random.choice(funcs)
print(linear(5))
