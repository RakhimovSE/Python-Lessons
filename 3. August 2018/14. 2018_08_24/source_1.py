def function(n, m):
	arr = []
	for i in range(n):
		arr.append([])
		for j in range(m):
			arr[i].append(0)
	return arr


def ways(arr, n, m, i, j):
	for j in range(m):
		arr[0][j] = 1
	for i in range(n):
		arr[i][0] = 1
	for i in range(1, n):
		for j in range(1, m):
			arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
	return arr[n - 1][m - 1]


if __name__ == '__main__':
	n = int(input())
	m = int(input())
	arr = function(n, m)
	i = 0
	j = 0
	print(ways(arr, n, m, i, j))
