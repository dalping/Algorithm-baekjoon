import sys
from copy import deepcopy
sys.setrecursionlimit(100000)

def DFS(x, y, h):
    if x < 0 or y < 0 or x >= N or y >= N:
        return False

    if graph_copy[x][y] > h:  # 물에 잠기지 않는 지점
        graph_copy[x][y] = 0
        DFS(x + 1, y, h)
        DFS(x - 1, y, h)
        DFS(x, y + 1, h)
        DFS(x, y - 1, h)
        return True
    return False

graph = []
graph_copy = []
h_max, h_min = 0, 100
count = 0
answer = 1 #아무곳도 잠기지 않을 경우

N = int(input())
for _ in range(N):
    s = list(map(int, input().split()))
    graph.append(s)

    if max(s) > h_max:
        h_max = max(s)
    if min(s) < h_min:
        h_min = min(s)

for k in range(h_min, h_max + 1):
    count = 0
    graph_copy = deepcopy(graph)
    for i in range(N):
        for j in range(N):
            if graph_copy[i][j] > k:
                count += 1
                DFS(i, j, k)
    if count > answer:
        answer = count

print(answer)