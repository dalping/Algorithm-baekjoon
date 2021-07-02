def DFS(n, s):
    if str(n) in s:
        return
    else:
        s += str(n)
        if len(s) == N:
            print(' '.join(list(s)))
            return

    for i in range(1, N + 1):
        DFS(str(i), s)

N = int(input())
answer = []

for i in range(1, N+1):
    DFS(str(i),'')
