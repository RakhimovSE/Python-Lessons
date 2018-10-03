import random

def gen_arr(n, m):
	arr = []
	for i in range(n):
		arr.append([])
		for j in range(m):
			arr[i].append(random.randint(-10, 10))
	return arr


def print_arr(arr, n, m):
        for i in range(n):
                st = ''
                for j in range(m):
                        st += '%4d' % arr[i][j]
                print(st)


def ways(arr, n, m):
	for j in range(1, m):
		arr[0][j] += arr[0][j - 1]
	for i in range(1, n):
		arr[i][0] += arr[i - 1][0]
	for i in range(1, n):
		for j in range(1, m):
			arr[i][j] += min(arr[i - 1][j], arr[i][j - 1], arr[i - 1][j - 1])
	return arr[n - 1][m - 1]


if __name__ == '__main__':
	n = int(input())
	m = int(input())
	arr = gen_arr(n, m)
	print_arr(arr, n, m)
	print(ways(arr, n, m))
