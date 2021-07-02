from collections import deque
import sys
input = sys.stdin.readline

def DFS(x, y, L):
    global answer

    #범위 바깥이거나 가본적 있는 알파벳
    if (x < 0 or y < 0 or x >= N or y >= M):
        if len(L) > answer:
            answer = len(L)
        return False

    if graph[x][y] in L:
        if len(L) > answer:
            answer = len(L)
        return False

    else:
        L += graph[x][y]

        for k in range(4):
            DFS(x + dx[k], y + dy[k], L)
        return True
    return False

N, M = list(map(int, input().rstrip().split()))
graph = []
answer = 0
dx = [1 ,-1 ,0 ,0]
dy = [0 ,0 ,1 ,-1]
for _ in range(N):
    graph.append(list(input().rstrip()))

DFS(0,0,'')
print(answer)

