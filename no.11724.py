import sys
from collections import deque
input = sys.stdin.readline

def BFS(n):
    queue = deque()
    queue.append(n)

    while queue:
        val = queue.popleft()
        if visited[val] == False:
            visited[val] = True
            for i in node[val]:
                queue.append(i)

N, M = list(map(int, input().rstrip().split()))
node = [[] for i in range(N + 1)]
visited = [False] * (N + 1)
answer = 0

for i in range(M):
    a, b = list(map(int, input().rstrip().split()))
    node[a].append(b)
    node[b].append(a)

for i in range(1, N + 1):
    if visited[i] == False:
        BFS(i)
        answer += 1

print(answer)

