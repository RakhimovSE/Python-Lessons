sum = 0
mas = [0 for i in range(1000001)]
N, a = int(input()), []
for i in range(N):
    x = int(input())
    if len(a) == 0 or x != a[-1]:
        a.append(x)

M = int(input())
for i in range(M):
    mas[int(input())] += 1
for i in range(N):
    sum += mas[a[i]]
print(sum)