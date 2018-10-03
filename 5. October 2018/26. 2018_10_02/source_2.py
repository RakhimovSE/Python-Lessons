def f1(x):
    print('f1: ', end='')
    return 2 * x ** 2 - 4 * x + 1

def f2(x):
    print('f2: ', end='')
    return 1 / x

f = f1

print(f(5))
print(f1(5))
print(f2(5))
print()

f = f2

print(f(5))
print(f1(5))
print(f2(5))
