#유기농 배추
import sys
sys.setrecursionlimit(100000)

def DFS(x, y):
    if x < 0 or y < 0 or x >= N or y >= M:
        return False
    if graph[x][y] == 0:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        DFS(x + 1, y)
        DFS(x - 1, y)
        DFS(x, y + 1)
        DFS(x, y - 1)
        return True
    return False

T = int(input())

for _ in range(T):

    M, N, K = list(map(int, input().split())) #가로, 세로, 배추 수
    graph = [[0 for i in range(M)] for i in range(N)]
    answer = 0

    for i in range(K):
        x, y = list(map(int, input().split()))
        graph[y][x] = 1

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                DFS(i, j)
                answer += 1
    print(answer)

