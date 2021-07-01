import sys

input = sys.stdin.readline
K = int(input())
arr = []
for i in range(K):
    s = int(input())
    if s == 0:
        arr.pop()
    else:
        arr.append(s)

print(sum(arr))