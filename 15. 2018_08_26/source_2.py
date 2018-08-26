import random

def randword(n=5):
    result = ''
    for i in range(n):
        result += chr(random.randint(ord('a'), ord('z')))
    return result

print(randword(10))
