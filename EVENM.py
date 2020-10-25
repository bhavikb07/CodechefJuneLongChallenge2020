from sys import stdin
from math import ceil, gcd

# Input data
#stdin = open("input", "r")


def answer(mat):
    for i in range(n):
        print(*mat[i])

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    #n, k = map(int, stdin.readline().split())
    #arr = list(map(int, stdin.readline().split()))
    #s = stdin.readline().strip()
    arr = [[0 for i in range(n)] for j in range(n)]
    a = 1
    for i in range(n):
        if i % 2 == 0:
            for j in range(n):
                arr[i][j] = a
                a += 1
        else:
            for j in range(n - 1, -1, -1):
                arr[i][j] = a
                a += 1
    for i in range(n):
        print(*arr[i])
