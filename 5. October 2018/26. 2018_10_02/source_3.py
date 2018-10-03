# Callback-фунция - передача функции как параметр

def myfunc(x):
    raw = int(x)
    if raw > 0:
        return 1
    if raw < 0:
        return -1
    return 0

def azaza(x):
    return myfunc(x)

# примерный алгоритм работы функции map
# передаем в нее ссылку на функцию и массив
# прогоняем каждый элемент через переданную функцию
def mymap(func, elements):
    result = []
    for element in elements:
        result.append(func(element))
    return result

inp = input().split()

res = list(map(myfunc, inp))
res2 = mymap(myfunc, inp)

key = lambda x: int(x) ** 2

res3 = list(map(key, inp))
print(res)
print(res2)
print(res3)
