n, m = list(map(int, input().split()))
r, s = 1, 1

for i in range(n, n-m, -1):
    r *= i

for j in range(m, 0, -1):
    s *= j

print(r//s)